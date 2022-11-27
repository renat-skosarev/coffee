import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QWidget

QUERY = 'SELECT variety_name, roast, ground_or_beans, description, price, package_size FROM coffee;'


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('main.ui', self)

        self.con = sqlite3.connect('coffee.sqlite')
        self.cur = self.con.cursor()

        self.update_button.clicked.connect(self.update_table)
        self.edit_button.clicked.connect(self.edit)
        self.add_button.clicked.connect(self.add)
        self.update_table()

    def get_data(self):
        data = self.cur.execute(QUERY).fetchall()
        return data

    def update_table(self):
        data = self.get_data()
        self.table.setColumnCount(6)
        self.table.setRowCount(len(data))
        self.table.setHorizontalHeaderLabels(
            ['Variety name', 'Roast level', 'Type', 'Description', 'Price [rub]', 'Size [kg]'])
        for row in range(len(data)):
            for col in range(6):
                self.table.setItem(row, col, QTableWidgetItem(str(data[row][col])))

    def add(self):
        pass

    def edit(self):
        self.form = AddEditCoffeeForm()
        self.form.show()


class AddEditCoffeeForm(QWidget):
    def __init__(self):
        super(AddEditCoffeeForm, self).__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
