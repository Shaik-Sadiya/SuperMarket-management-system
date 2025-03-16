# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'supermarket.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1057, 861)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 921, 831))
        self.frame.setStyleSheet("background-color: rgb(212, 0, 159);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(260, 50, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setGeometry(QtCore.QRect(30, 110, 861, 651))
        self.tabWidget.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(30, 130, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(30, 230, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(30, 380, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(30, 280, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(30, 180, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(30, 330, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(30, 430, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.id = QtWidgets.QLineEdit(self.tab)
        self.id.setGeometry(QtCore.QRect(200, 40, 161, 22))
        self.id.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.id.setObjectName("id")
        self.product = QtWidgets.QPushButton(self.tab)
        self.product.setGeometry(QtCore.QRect(500, 30, 141, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.product.setFont(font)
        self.product.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.product.setObjectName("product")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.tab)
        self.calendarWidget.setGeometry(QtCore.QRect(390, 100, 431, 271))
        self.calendarWidget.setStyleSheet("background-color: rgb(128, 126, 143);")
        self.calendarWidget.setObjectName("calendarWidget")
        self.name = QtWidgets.QLineEdit(self.tab)
        self.name.setGeometry(QtCore.QRect(200, 80, 161, 22))
        self.name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.name.setObjectName("name")
        self.quantity = QtWidgets.QLineEdit(self.tab)
        self.quantity.setGeometry(QtCore.QRect(200, 130, 161, 22))
        self.quantity.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.quantity.setObjectName("quantity")
        self.price = QtWidgets.QLineEdit(self.tab)
        self.price.setGeometry(QtCore.QRect(200, 180, 161, 22))
        self.price.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.price.setObjectName("price")
        self.vendname = QtWidgets.QLineEdit(self.tab)
        self.vendname.setGeometry(QtCore.QRect(200, 240, 161, 22))
        self.vendname.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.vendname.setObjectName("vendname")
        self.vendnumber = QtWidgets.QLineEdit(self.tab)
        self.vendnumber.setGeometry(QtCore.QRect(200, 290, 161, 22))
        self.vendnumber.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.vendnumber.setObjectName("vendnumber")
        self.arrival = QtWidgets.QLineEdit(self.tab)
        self.arrival.setGeometry(QtCore.QRect(200, 390, 161, 22))
        self.arrival.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.arrival.setObjectName("arrival")
        self.expire = QtWidgets.QLineEdit(self.tab)
        self.expire.setGeometry(QtCore.QRect(200, 440, 161, 22))
        self.expire.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.expire.setObjectName("expire")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(200, 340, 161, 22))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.submit = QtWidgets.QPushButton(self.tab)
        self.submit.setGeometry(QtCore.QRect(30, 490, 91, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.submit.setFont(font)
        self.submit.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"background-color: rgb(176, 232, 255);")
        self.submit.setObjectName("submit")
        self.reset = QtWidgets.QPushButton(self.tab)
        self.reset.setGeometry(QtCore.QRect(140, 490, 91, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reset.setFont(font)
        self.reset.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"background-color: rgb(0, 255, 255);")
        self.reset.setObjectName("reset")
        self.DE = QtWidgets.QPushButton(self.tab)
        self.DE.setGeometry(QtCore.QRect(390, 430, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DE.setFont(font)
        self.DE.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"background-color: rgb(229, 153, 0);")
        self.DE.setObjectName("DE")
        self.DA = QtWidgets.QPushButton(self.tab)
        self.DA.setGeometry(QtCore.QRect(390, 390, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DA.setFont(font)
        self.DA.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"background-color: rgb(255, 194, 232);")
        self.DA.setObjectName("DA")
        self.update = QtWidgets.QPushButton(self.tab)
        self.update.setGeometry(QtCore.QRect(250, 490, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.update.setFont(font)
        self.update.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"background-color: rgb(255, 170, 0);")
        self.update.setObjectName("update")
        self.delete_2 = QtWidgets.QPushButton(self.tab)
        self.delete_2.setGeometry(QtCore.QRect(30, 550, 141, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.delete_2.setFont(font)
        self.delete_2.setStyleSheet("background-color: rgb(85, 85, 255);")
        self.delete_2.setObjectName("delete_2")
        self.exit = QtWidgets.QPushButton(self.tab)
        self.exit.setGeometry(QtCore.QRect(210, 550, 141, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.exit.setFont(font)
        self.exit.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.exit.setObjectName("exit")
        self.tabWidget.addTab(self.tab, "")
        self.ViewStock = QtWidgets.QWidget()
        self.ViewStock.setObjectName("ViewStock")
        self.textEdit = QtWidgets.QTextEdit(self.ViewStock)
        self.textEdit.setGeometry(QtCore.QRect(50, 160, 751, 391))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.label_11 = QtWidgets.QLabel(self.ViewStock)
        self.label_11.setGeometry(QtCore.QRect(60, 90, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.ViewStock)
        self.label_12.setGeometry(QtCore.QRect(340, 90, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.ViewStock)
        self.lineEdit_10.setGeometry(QtCore.QRect(200, 90, 113, 31))
        self.lineEdit_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.ViewStock)
        self.lineEdit_11.setGeometry(QtCore.QRect(450, 90, 113, 31))
        self.lineEdit_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.add = QtWidgets.QPushButton(self.ViewStock)
        self.add.setGeometry(QtCore.QRect(670, 90, 93, 28))
        self.add.setStyleSheet("background-color: rgb(234, 234, 175);")
        self.add.setObjectName("add")
        self.label_13 = QtWidgets.QLabel(self.ViewStock)
        self.label_13.setGeometry(QtCore.QRect(190, 580, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.tabWidget.addTab(self.ViewStock, "")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.view = QtWidgets.QPushButton(self.widget)
        self.view.setGeometry(QtCore.QRect(390, 50, 93, 28))
        self.view.setStyleSheet("background-color: rgb(238, 238, 178);")
        self.view.setObjectName("view")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 130, 751, 441))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(137, 170, 165);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tabWidget.addTab(self.widget, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Organic Super Market"))
        self.label_2.setText(_translate("MainWindow", "Product ID"))
        self.label_3.setText(_translate("MainWindow", "Product Name"))
        self.label_4.setText(_translate("MainWindow", "Quantity"))
        self.label_5.setText(_translate("MainWindow", "Vendor Name"))
        self.label_6.setText(_translate("MainWindow", "Date of Arrival"))
        self.label_7.setText(_translate("MainWindow", "Vendor Number"))
        self.label_8.setText(_translate("MainWindow", "Price"))
        self.label_9.setText(_translate("MainWindow", "Mfg Place"))
        self.label_10.setText(_translate("MainWindow", "Date of Expire"))
        self.product.setText(_translate("MainWindow", "Product Details"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Andhra Pradesh"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Goa"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Tamilnadu"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Uttar Pradesh"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Hyderabad"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.reset.setText(_translate("MainWindow", "Reset"))
        self.DE.setText(_translate("MainWindow", "DE"))
        self.DA.setText(_translate("MainWindow", "DA"))
        self.update.setText(_translate("MainWindow", "Update"))
        self.delete_2.setText(_translate("MainWindow", "Delete"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Stock Entry"))
        self.label_11.setText(_translate("MainWindow", "Product ID"))
        self.label_12.setText(_translate("MainWindow", "Quantity"))
        self.add.setText(_translate("MainWindow", "ADD"))
        self.label_13.setText(_translate("MainWindow", "Total bill"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ViewStock), _translate("MainWindow", "Billing"))
        self.view.setText(_translate("MainWindow", "View Stock"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Product Id"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Product name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Vendor Number"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("MainWindow", "View Stock"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
