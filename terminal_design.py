# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Terminal.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1032, 538)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.LblBaudrate = QtWidgets.QLabel(self.centralwidget)
        self.LblBaudrate.setObjectName("LblBaudrate")
        self.gridLayout.addWidget(self.LblBaudrate, 6, 3, 1, 1)
        self.CBBaudrate = QtWidgets.QComboBox(self.centralwidget)
        self.CBBaudrate.setObjectName("CBBaudrate")
        self.CBBaudrate.addItem("")
        self.CBBaudrate.addItem("")
        self.CBBaudrate.addItem("")
        self.CBBaudrate.addItem("")
        self.gridLayout.addWidget(self.CBBaudrate, 6, 4, 1, 1)
        self.CBPorts = QtWidgets.QComboBox(self.centralwidget)
        self.CBPorts.setMinimumSize(QtCore.QSize(300, 0))
        self.CBPorts.setObjectName("CBPorts")
        self.gridLayout.addWidget(self.CBPorts, 0, 2, 1, 3)
        self.LblAvailable = QtWidgets.QLabel(self.centralwidget)
        self.LblAvailable.setObjectName("LblAvailable")
        self.gridLayout.addWidget(self.LblAvailable, 0, 1, 1, 1)
        self.BtnReScan = QtWidgets.QPushButton(self.centralwidget)
        self.BtnReScan.setObjectName("BtnReScan")
        self.gridLayout.addWidget(self.BtnReScan, 0, 0, 1, 1)
        self.LblCounter = QtWidgets.QLabel(self.centralwidget)
        self.LblCounter.setMaximumSize(QtCore.QSize(55, 16777215))
        self.LblCounter.setObjectName("LblCounter")
        self.gridLayout.addWidget(self.LblCounter, 12, 1, 1, 1)
        self.BtnCounter = QtWidgets.QPushButton(self.centralwidget)
        self.BtnCounter.setObjectName("BtnCounter")
        self.gridLayout.addWidget(self.BtnCounter, 12, 0, 1, 1)
        self.LblCounterData = QtWidgets.QLabel(self.centralwidget)
        self.LblCounterData.setObjectName("LblCounterData")
        self.gridLayout.addWidget(self.LblCounterData, 12, 2, 1, 1)
        self.BtnConnect = QtWidgets.QPushButton(self.centralwidget)
        self.BtnConnect.setEnabled(False)
        self.BtnConnect.setObjectName("BtnConnect")
        self.gridLayout.addWidget(self.BtnConnect, 6, 0, 1, 1)
        self.BtnSave = QtWidgets.QPushButton(self.centralwidget)
        self.BtnSave.setObjectName("BtnSave")
        self.gridLayout.addWidget(self.BtnSave, 12, 3, 1, 1)
        self.LblStatusInfo = QtWidgets.QLabel(self.centralwidget)
        self.LblStatusInfo.setObjectName("LblStatusInfo")
        self.gridLayout.addWidget(self.LblStatusInfo, 0, 6, 1, 1)
        self.BtnDisconnect = QtWidgets.QPushButton(self.centralwidget)
        self.BtnDisconnect.setEnabled(False)
        self.BtnDisconnect.setObjectName("BtnDisconnect")
        self.gridLayout.addWidget(self.BtnDisconnect, 7, 0, 1, 1)
        self.LblStatus = QtWidgets.QLabel(self.centralwidget)
        self.LblStatus.setObjectName("LblStatus")
        self.gridLayout.addWidget(self.LblStatus, 0, 5, 1, 1)
        self.CBSTM = QtWidgets.QCheckBox(self.centralwidget)
        self.CBSTM.setChecked(True)
        self.CBSTM.setObjectName("CBSTM")
        self.gridLayout.addWidget(self.CBSTM, 6, 2, 1, 1)
        self.BtnMacros7 = QtWidgets.QPushButton(self.centralwidget)
        self.BtnMacros7.setEnabled(False)
        self.BtnMacros7.setObjectName("BtnMacros7")
        self.gridLayout.addWidget(self.BtnMacros7, 15, 9, 1, 1)
        self.BtnMacros10 = QtWidgets.QPushButton(self.centralwidget)
        self.BtnMacros10.setEnabled(False)
        self.BtnMacros10.setObjectName("BtnMacros10")
        self.gridLayout.addWidget(self.BtnMacros10, 18, 9, 1, 1)
        self.BtnMacros9 = QtWidgets.QPushButton(self.centralwidget)
        self.BtnMacros9.setEnabled(False)
        self.BtnMacros9.setObjectName("BtnMacros9")
        self.gridLayout.addWidget(self.BtnMacros9, 17, 9, 1, 1)
        self.BtnMacros8 = QtWidgets.QPushButton(self.centralwidget)
        self.BtnMacros8.setEnabled(False)
        self.BtnMacros8.setObjectName("BtnMacros8")
        self.gridLayout.addWidget(self.BtnMacros8, 16, 9, 1, 1)
        self.BtnMacros11 = QtWidgets.QPushButton(self.centralwidget)
        self.BtnMacros11.setEnabled(False)
        self.BtnMacros11.setObjectName("BtnMacros11")
        self.gridLayout.addWidget(self.BtnMacros11, 0, 10, 1, 1)
        self.LblTransmit = QtWidgets.QLabel(self.centralwidget)
        self.LblTransmit.setObjectName("LblTransmit")
        self.gridLayout.addWidget(self.LblTransmit, 22, 0, 1, 1)
        self.BtnMacros12 = QtWidgets.QPushButton(self.centralwidget)
        self.BtnMacros12.setEnabled(False)
        self.BtnMacros12.setObjectName("BtnMacros12")
        self.gridLayout.addWidget(self.BtnMacros12, 6, 10, 1, 1)
        self.BtnMacros13 = QtWidgets.QPushButton(self.centralwidget)
        self.BtnMacros13.setEnabled(False)
        self.BtnMacros13.setObjectName("BtnMacros13")
        self.gridLayout.addWidget(self.BtnMacros13, 7, 10, 1, 1)
        self.BtnMacros15 = QtWidgets.QPushButton(self.centralwidget)
        self.BtnMacros15.setEnabled(False)
        self.BtnMacros15.setObjectName("BtnMacros15")
        self.gridLayout.addWidget(self.BtnMacros15, 13, 10, 1, 1)
        self.BtnMacros14 = QtWidgets.QPushButton(self.centralwidget)
        self.BtnMacros14.setEnabled(False)
        self.BtnMacros14.setObjectName("BtnMacros14")
        self.gridLayout.addWidget(self.BtnMacros14, 12, 10, 1, 1)
        self.BtnMacros6 = QtWidgets.QPushButton(self.centralwidget)
        self.BtnMacros6.setEnabled(False)
        self.BtnMacros6.setObjectName("BtnMacros6")
        self.gridLayout.addWidget(self.BtnMacros6, 14, 9, 1, 1)
        self.BtnMacros18 = QtWidgets.QPushButton(self.centralwidget)
        self.BtnMacros18.setEnabled(False)
        self.BtnMacros18.setObjectName("BtnMacros18")
        self.gridLayout.addWidget(self.BtnMacros18, 16, 10, 1, 1)
        self.BtnMacros16 = QtWidgets.QPushButton(self.centralwidget)
        self.BtnMacros16.setEnabled(False)
        self.BtnMacros16.setObjectName("BtnMacros16")
        self.gridLayout.addWidget(self.BtnMacros16, 14, 10, 1, 1)
        self.BtnMacros19 = QtWidgets.QPushButton(self.centralwidget)
        self.BtnMacros19.setEnabled(False)
        self.BtnMacros19.setObjectName("BtnMacros19")
        self.gridLayout.addWidget(self.BtnMacros19, 17, 10, 1, 1)
        self.BtnMacros17 = QtWidgets.QPushButton(self.centralwidget)
        self.BtnMacros17.setEnabled(False)
        self.BtnMacros17.setObjectName("BtnMacros17")
        self.gridLayout.addWidget(self.BtnMacros17, 15, 10, 1, 1)
        self.BtnMacros1_2 = QtWidgets.QPushButton(self.centralwidget)
        self.BtnMacros1_2.setEnabled(False)
        self.BtnMacros1_2.setObjectName("BtnMacros1_2")
        self.gridLayout.addWidget(self.BtnMacros1_2, 6, 9, 1, 1)
        self.BtnMacros4 = QtWidgets.QPushButton(self.centralwidget)
        self.BtnMacros4.setEnabled(False)
        self.BtnMacros4.setObjectName("BtnMacros4")
        self.gridLayout.addWidget(self.BtnMacros4, 12, 9, 1, 1)
        self.CBMacros = QtWidgets.QComboBox(self.centralwidget)
        self.CBMacros.setObjectName("CBMacros")
        self.gridLayout.addWidget(self.CBMacros, 20, 9, 1, 2)
        self.BtnMacros5 = QtWidgets.QPushButton(self.centralwidget)
        self.BtnMacros5.setEnabled(False)
        self.BtnMacros5.setObjectName("BtnMacros5")
        self.gridLayout.addWidget(self.BtnMacros5, 13, 9, 1, 1)
        self.BtnSend = QtWidgets.QPushButton(self.centralwidget)
        self.BtnSend.setEnabled(False)
        self.BtnSend.setObjectName("BtnSend")
        self.gridLayout.addWidget(self.BtnSend, 22, 4, 1, 1)
        self.BtnMacros3 = QtWidgets.QPushButton(self.centralwidget)
        self.BtnMacros3.setEnabled(False)
        self.BtnMacros3.setObjectName("BtnMacros3")
        self.gridLayout.addWidget(self.BtnMacros3, 7, 9, 1, 1)
        self.BtnMacros20 = QtWidgets.QPushButton(self.centralwidget)
        self.BtnMacros20.setEnabled(False)
        self.BtnMacros20.setObjectName("BtnMacros20")
        self.gridLayout.addWidget(self.BtnMacros20, 18, 10, 1, 1)
        self.TxtTransmit = QtWidgets.QLineEdit(self.centralwidget)
        self.TxtTransmit.setObjectName("TxtTransmit")
        self.gridLayout.addWidget(self.TxtTransmit, 22, 1, 1, 3)
        self.BtnClear = QtWidgets.QPushButton(self.centralwidget)
        self.BtnClear.setObjectName("BtnClear")
        self.gridLayout.addWidget(self.BtnClear, 22, 7, 1, 1)
        self.CBClear = QtWidgets.QCheckBox(self.centralwidget)
        self.CBClear.setChecked(True)
        self.CBClear.setObjectName("CBClear")
        self.gridLayout.addWidget(self.CBClear, 22, 5, 1, 2)
        self.BtnMacros1 = QtWidgets.QPushButton(self.centralwidget)
        self.BtnMacros1.setEnabled(False)
        self.BtnMacros1.setObjectName("BtnMacros1")
        self.gridLayout.addWidget(self.BtnMacros1, 0, 9, 1, 1)
        self.LblMacrosAvailable = QtWidgets.QLabel(self.centralwidget)
        self.LblMacrosAvailable.setObjectName("LblMacrosAvailable")
        self.gridLayout.addWidget(self.LblMacrosAvailable, 19, 9, 1, 2)
        self.TxtBuffer = QtWidgets.QTextBrowser(self.centralwidget)
        self.TxtBuffer.setObjectName("TxtBuffer")
        self.gridLayout.addWidget(self.TxtBuffer, 13, 0, 9, 9)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 21, 9, 1, 2)
        self.BtnCreateMacros = QtWidgets.QPushButton(self.centralwidget)
        self.BtnCreateMacros.setObjectName("BtnCreateMacros")
        self.gridLayout.addWidget(self.BtnCreateMacros, 22, 9, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1032, 26))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.menuSettings.addAction(self.actionSettings)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.CBSTM, self.BtnReScan)
        MainWindow.setTabOrder(self.BtnReScan, self.CBPorts)
        MainWindow.setTabOrder(self.CBPorts, self.CBBaudrate)
        MainWindow.setTabOrder(self.CBBaudrate, self.BtnConnect)
        MainWindow.setTabOrder(self.BtnConnect, self.BtnDisconnect)
        MainWindow.setTabOrder(self.BtnDisconnect, self.BtnCounter)
        MainWindow.setTabOrder(self.BtnCounter, self.BtnSave)
        MainWindow.setTabOrder(self.BtnSave, self.TxtTransmit)
        MainWindow.setTabOrder(self.TxtTransmit, self.BtnSend)
        MainWindow.setTabOrder(self.BtnSend, self.CBClear)
        MainWindow.setTabOrder(self.CBClear, self.BtnClear)
        MainWindow.setTabOrder(self.BtnClear, self.BtnMacros1)
        MainWindow.setTabOrder(self.BtnMacros1, self.BtnMacros11)
        MainWindow.setTabOrder(self.BtnMacros11, self.BtnMacros1_2)
        MainWindow.setTabOrder(self.BtnMacros1_2, self.BtnMacros12)
        MainWindow.setTabOrder(self.BtnMacros12, self.BtnMacros3)
        MainWindow.setTabOrder(self.BtnMacros3, self.BtnMacros13)
        MainWindow.setTabOrder(self.BtnMacros13, self.BtnMacros4)
        MainWindow.setTabOrder(self.BtnMacros4, self.BtnMacros14)
        MainWindow.setTabOrder(self.BtnMacros14, self.BtnMacros5)
        MainWindow.setTabOrder(self.BtnMacros5, self.BtnMacros15)
        MainWindow.setTabOrder(self.BtnMacros15, self.BtnMacros6)
        MainWindow.setTabOrder(self.BtnMacros6, self.BtnMacros16)
        MainWindow.setTabOrder(self.BtnMacros16, self.BtnMacros7)
        MainWindow.setTabOrder(self.BtnMacros7, self.BtnMacros17)
        MainWindow.setTabOrder(self.BtnMacros17, self.BtnMacros8)
        MainWindow.setTabOrder(self.BtnMacros8, self.BtnMacros18)
        MainWindow.setTabOrder(self.BtnMacros18, self.BtnMacros9)
        MainWindow.setTabOrder(self.BtnMacros9, self.BtnMacros19)
        MainWindow.setTabOrder(self.BtnMacros19, self.BtnMacros10)
        MainWindow.setTabOrder(self.BtnMacros10, self.BtnMacros20)
        MainWindow.setTabOrder(self.BtnMacros20, self.CBMacros)
        MainWindow.setTabOrder(self.CBMacros, self.BtnCreateMacros)
        MainWindow.setTabOrder(self.BtnCreateMacros, self.TxtBuffer)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OstrannaTerminal"))
        self.LblBaudrate.setText(_translate("MainWindow", "Baudrate:"))
        self.CBBaudrate.setItemText(0, _translate("MainWindow", "9600"))
        self.CBBaudrate.setItemText(1, _translate("MainWindow", "115200"))
        self.CBBaudrate.setItemText(2, _translate("MainWindow", "256000"))
        self.CBBaudrate.setItemText(3, _translate("MainWindow", "Custom"))
        self.LblAvailable.setText(_translate("MainWindow", "COMs Available:"))
        self.BtnReScan.setText(_translate("MainWindow", "ReScan"))
        self.LblCounter.setText(_translate("MainWindow", "Counter:"))
        self.BtnCounter.setText(_translate("MainWindow", "Clear Counter"))
        self.LblCounterData.setText(_translate("MainWindow", "0"))
        self.BtnConnect.setText(_translate("MainWindow", "Connect"))
        self.BtnSave.setText(_translate("MainWindow", "Save to log"))
        self.LblStatusInfo.setText(_translate("MainWindow", "Not Connected"))
        self.BtnDisconnect.setText(_translate("MainWindow", "Disconnect"))
        self.LblStatus.setText(_translate("MainWindow", "Status:"))
        self.CBSTM.setText(_translate("MainWindow", "STM devices only"))
        self.BtnMacros7.setText(_translate("MainWindow", "M7"))
        self.BtnMacros10.setText(_translate("MainWindow", "M10"))
        self.BtnMacros9.setText(_translate("MainWindow", "M9"))
        self.BtnMacros8.setText(_translate("MainWindow", "M8"))
        self.BtnMacros11.setText(_translate("MainWindow", "M11"))
        self.LblTransmit.setText(_translate("MainWindow", "Transmit:"))
        self.BtnMacros12.setText(_translate("MainWindow", "M12"))
        self.BtnMacros13.setText(_translate("MainWindow", "M13"))
        self.BtnMacros15.setText(_translate("MainWindow", "M15"))
        self.BtnMacros14.setText(_translate("MainWindow", "M14"))
        self.BtnMacros6.setText(_translate("MainWindow", "M6"))
        self.BtnMacros18.setText(_translate("MainWindow", "M18"))
        self.BtnMacros16.setText(_translate("MainWindow", "M16"))
        self.BtnMacros19.setText(_translate("MainWindow", "M19"))
        self.BtnMacros17.setText(_translate("MainWindow", "M17"))
        self.BtnMacros1_2.setText(_translate("MainWindow", "M2"))
        self.BtnMacros4.setText(_translate("MainWindow", "M4"))
        self.BtnMacros5.setText(_translate("MainWindow", "M5"))
        self.BtnSend.setText(_translate("MainWindow", "Send"))
        self.BtnMacros3.setText(_translate("MainWindow", "M3"))
        self.BtnMacros20.setText(_translate("MainWindow", "M20"))
        self.BtnClear.setText(_translate("MainWindow", "Clear"))
        self.CBClear.setText(_translate("MainWindow", "Clear after sending"))
        self.BtnMacros1.setText(_translate("MainWindow", "M1"))
        self.LblMacrosAvailable.setText(_translate("MainWindow", "Macros sets available"))
        self.TxtBuffer.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Macros not selected"))
        self.BtnCreateMacros.setText(_translate("MainWindow", "Create Set"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))

