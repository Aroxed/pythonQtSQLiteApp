import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QApplication, QDialog


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('demo.ui', self)
        self.pushButton.clicked.connect(self.generateData)

    def generateData(self):
        # Create SQLite database
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('data.db')
        if not db.open():
            print("Error: Could not open database.")
            return

        # Generate random data and populate ListWidget
        query = QSqlQuery()
        query.exec_("CREATE TABLE IF NOT EXISTS data (value INTEGER)")
        query.exec_("DELETE FROM data")
        for _ in range(10):
            value = randint(1, 100)
            query.exec_("INSERT INTO data (value) VALUES ({})".format(value))
            self.listWidget.addItem(str(value))

        db.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
