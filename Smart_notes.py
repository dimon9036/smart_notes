import json
from PyQt5 import QtCore, QtGui, QtWidgets

notes = {}

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(883, 578)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 521, 521))
        self.textEdit.setObjectName("textEdit")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(540, 30, 311, 161))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(540, 10, 101, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(540, 200, 151, 21))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(700, 200, 151, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(540, 230, 311, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(540, 260, 101, 16))
        self.label_2.setObjectName("label_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(540, 280, 311, 161))
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(540, 450, 311, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(540, 480, 151, 21))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(700, 480, 151, 21))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(540, 510, 311, 21))
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 883, 24))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menu.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.show_notes()
        
        self.listWidget.itemClicked.connect(self.show)
        self.pushButton.clicked.connect(self.create_note)
        self.pushButton_2.clicked.connect(self.del_note)
        self.pushButton_3.clicked.connect(self.save_note)
        self.pushButton_4.clicked.connect(self.add_tag)
        self.pushButton_5.clicked.connect(self.remove_tag)
        self.pushButton_6.clicked.connect(self.search_by_tag)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Список заміток"))
        self.pushButton.setText(_translate("MainWindow", "Створити замітку"))
        self.pushButton_2.setText(_translate("MainWindow", "Видалити замітку"))
        self.pushButton_3.setText(_translate("MainWindow", "Зберегти замітку"))
        self.label_2.setText(_translate("MainWindow", "Список тегів"))
        self.lineEdit.setText(_translate("MainWindow", "Введіть тег..."))
        self.pushButton_4.setText(_translate("MainWindow", "Додати до замітки"))
        self.pushButton_5.setText(_translate("MainWindow", "Відкріпити від замітки"))
        self.pushButton_6.setText(_translate("MainWindow", "Шукати замітки по тегу"))
        self.menu.setTitle(_translate("MainWindow", "Розумні замітки"))

    def show_notes(self):
        global notes
        with open("notes.json", "r", encoding="utf-8") as file:
            notes = json.load(file)
        self.listWidget.clear()
        self.listWidget.addItems(notes.keys())

    def show(self):
        key = self.listWidget.currentItem().text()
        self.textEdit.setText(notes[key]["текст"])
        self.listWidget_2.clear()
        self.listWidget_2.addItems(notes[key]["теги"])

    def create_note(self):
        new_note_name = f"Нова замітка {len(notes) + 1}"
        notes[new_note_name] = {"текст": "", "теги": []}
        with open("notes.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, ensure_ascii=False, indent=4)
        self.show_notes()

    def del_note(self):
        if self.listWidget.currentItem():
            key = self.listWidget.currentItem().text()
            del notes[key]
            with open("notes.json", "w", encoding="utf-8") as file:
                json.dump(notes, file, ensure_ascii=False, indent=4)
            self.show_notes()

    def save_note(self):
        if self.listWidget.currentItem():
            key = self.listWidget.currentItem().text()
            edited_text = self.textEdit.toPlainText()
            notes[key]["текст"] = edited_text
            with open("notes.json", "w", encoding="utf-8") as file:
                json.dump(notes, file, ensure_ascii=False, indent=4)

    def add_tag(self):
        if self.listWidget.currentItem():
            key = self.listWidget.currentItem().text()
            tag = self.lineEdit.text()
            if tag and tag not in notes[key]["теги"]:
                notes[key]["теги"].append(tag)
                self.listWidget_2.addItem(tag)
                self.lineEdit.clear()
            with open("notes.json", "w", encoding="utf-8") as file:
                json.dump(notes, file, ensure_ascii=False, indent=4)

    def remove_tag(self):
        if self.listWidget.currentItem() and self.listWidget_2.currentItem():
            key = self.listWidget.currentItem().text()
            tag = self.listWidget_2.currentItem().text()
            notes[key]["теги"].remove(tag)
            with open("notes.json", "w", encoding="utf-8") as file:
                json.dump(notes, file, ensure_ascii=False, indent=4)
            self.listWidget_2.clear()
            self.listWidget_2.addItems(notes[key]["теги"])

    def search_by_tag(self):
        tag = self.lineEdit.text()
        if tag:
            self.listWidget.clear()
            for note, content in notes.items():
                if tag in content["теги"]:
                    self.listWidget.addItem(note)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())