# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'poseVideo.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_poseVideoClass(object):
    def setupUi(self, poseVideoClass):
        poseVideoClass.setObjectName("poseVideoClass")
        poseVideoClass.resize(1118, 748)
        self.centralWidget = QtWidgets.QWidget(poseVideoClass)
        self.centralWidget.setObjectName("centralWidget")
        self.slider = QtWidgets.QSlider(self.centralWidget)
        self.slider.setGeometry(QtCore.QRect(20, 630, 961, 22))
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.display = QtWidgets.QLabel(self.centralWidget)
        self.display.setGeometry(QtCore.QRect(10, 10, 551, 551))
        self.display.setToolTipDuration(23)
        self.display.setFrameShape(QtWidgets.QFrame.Box)
        self.display.setText("")
        self.display.setObjectName("display")
        self.progresslabel = QtWidgets.QLabel(self.centralWidget)
        self.progresslabel.setGeometry(QtCore.QRect(1010, 630, 83, 16))
        self.progresslabel.setObjectName("progresslabel")
        self.playButton = QtWidgets.QPushButton(self.centralWidget)
        self.playButton.setGeometry(QtCore.QRect(150, 600, 75, 23))
        self.playButton.setObjectName("playButton")
        self.pauseButton = QtWidgets.QPushButton(self.centralWidget)
        self.pauseButton.setGeometry(QtCore.QRect(230, 600, 75, 23))
        self.pauseButton.setObjectName("pauseButton")
        self.browseButton = QtWidgets.QPushButton(self.centralWidget)
        self.browseButton.setGeometry(QtCore.QRect(70, 600, 75, 23))
        self.browseButton.setObjectName("browseButton")
        self.stopButton = QtWidgets.QPushButton(self.centralWidget)
        self.stopButton.setGeometry(QtCore.QRect(320, 600, 75, 23))
        self.stopButton.setObjectName("stopButton")
        self.doubleButton = QtWidgets.QPushButton(self.centralWidget)
        self.doubleButton.setGeometry(QtCore.QRect(410, 600, 75, 23))
        self.doubleButton.setObjectName("doubleButton")
        self.video2picsButton = QtWidgets.QPushButton(self.centralWidget)
        self.video2picsButton.setGeometry(QtCore.QRect(494, 600, 91, 23))
        self.video2picsButton.setObjectName("video2picsButton")
        self.readpicsButton = QtWidgets.QPushButton(self.centralWidget)
        self.readpicsButton.setGeometry(QtCore.QRect(590, 600, 91, 23))
        self.readpicsButton.setObjectName("readpicsButton")
        self.display2 = QtWidgets.QLabel(self.centralWidget)
        self.display2.setGeometry(QtCore.QRect(560, 10, 551, 551))
        self.display2.setToolTipDuration(23)
        self.display2.setFrameShape(QtWidgets.QFrame.Box)
        self.display2.setText("")
        self.display2.setObjectName("display2")
        self.playButton2 = QtWidgets.QPushButton(self.centralWidget)
        self.playButton2.setGeometry(QtCore.QRect(150, 650, 75, 23))
        self.playButton2.setObjectName("playButton2")
        self.stopButton2 = QtWidgets.QPushButton(self.centralWidget)
        self.stopButton2.setGeometry(QtCore.QRect(320, 650, 75, 23))
        self.stopButton2.setObjectName("stopButton2")
        self.doubleButton2 = QtWidgets.QPushButton(self.centralWidget)
        self.doubleButton2.setGeometry(QtCore.QRect(410, 650, 75, 23))
        self.doubleButton2.setObjectName("doubleButton2")
        self.pauseButton2 = QtWidgets.QPushButton(self.centralWidget)
        self.pauseButton2.setGeometry(QtCore.QRect(230, 650, 75, 23))
        self.pauseButton2.setObjectName("pauseButton2")
        self.browseButton2 = QtWidgets.QPushButton(self.centralWidget)
        self.browseButton2.setGeometry(QtCore.QRect(70, 650, 75, 23))
        self.browseButton2.setObjectName("browseButton2")
        self.comboBox = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox.setGeometry(QtCore.QRect(1000, 600, 104, 26))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(20, 600, 60, 21))
        self.label.setObjectName("label")
        self.label2 = QtWidgets.QLabel(self.centralWidget)
        self.label2.setGeometry(QtCore.QRect(20, 650, 60, 21))
        self.label2.setObjectName("label2")
        self.slider2 = QtWidgets.QSlider(self.centralWidget)
        self.slider2.setGeometry(QtCore.QRect(20, 680, 961, 22))
        self.slider2.setOrientation(QtCore.Qt.Horizontal)
        self.slider2.setObjectName("slider2")
        self.progresslabel2 = QtWidgets.QLabel(self.centralWidget)
        self.progresslabel2.setGeometry(QtCore.QRect(1010, 680, 83, 16))
        self.progresslabel2.setObjectName("progresslabel2")
        self.comboBox2 = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox2.setGeometry(QtCore.QRect(1000, 650, 104, 26))
        self.comboBox2.setObjectName("comboBox2")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.sendButton = QtWidgets.QPushButton(self.centralWidget)
        self.sendButton.setGeometry(QtCore.QRect(790, 600, 91, 23))
        self.sendButton.setObjectName("sendButton")
        poseVideoClass.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(poseVideoClass)
        self.mainToolBar.setObjectName("mainToolBar")
        poseVideoClass.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(poseVideoClass)
        self.statusBar.setObjectName("statusBar")
        poseVideoClass.setStatusBar(self.statusBar)
        self.toolBar = QtWidgets.QToolBar(poseVideoClass)
        self.toolBar.setObjectName("toolBar")
        poseVideoClass.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtWidgets.QAction(poseVideoClass)
        self.actionOpen.setObjectName("actionOpen")

        self.retranslateUi(poseVideoClass)
        QtCore.QMetaObject.connectSlotsByName(poseVideoClass)

    def retranslateUi(self, poseVideoClass):
        _translate = QtCore.QCoreApplication.translate
        poseVideoClass.setWindowTitle(_translate("poseVideoClass", "poseVideo"))
        self.progresslabel.setText(_translate("poseVideoClass", "Current / Total"))
        self.playButton.setText(_translate("poseVideoClass", "Play"))
        self.pauseButton.setText(_translate("poseVideoClass", "Pause"))
        self.browseButton.setText(_translate("poseVideoClass", "Browse"))
        self.stopButton.setText(_translate("poseVideoClass", "stop"))
        self.doubleButton.setText(_translate("poseVideoClass", "double"))
        self.video2picsButton.setText(_translate("poseVideoClass", "video2pics"))
        self.readpicsButton.setText(_translate("poseVideoClass", "readpics"))
        self.playButton2.setText(_translate("poseVideoClass", "Play"))
        self.stopButton2.setText(_translate("poseVideoClass", "stop"))
        self.doubleButton2.setText(_translate("poseVideoClass", "double"))
        self.pauseButton2.setText(_translate("poseVideoClass", "Pause"))
        self.browseButton2.setText(_translate("poseVideoClass", "Browse"))
        self.comboBox.setItemText(0, _translate("poseVideoClass", "30fps"))
        self.comboBox.setItemText(1, _translate("poseVideoClass", "25fps"))
        self.comboBox.setItemText(2, _translate("poseVideoClass", "20fps"))
        self.comboBox.setItemText(3, _translate("poseVideoClass", "15fps"))
        self.comboBox.setItemText(4, _translate("poseVideoClass", "10fps"))
        self.label.setText(_translate("poseVideoClass", "screen1"))
        self.label2.setText(_translate("poseVideoClass", "screen2"))
        self.progresslabel2.setText(_translate("poseVideoClass", "Current / Total"))
        self.comboBox2.setItemText(0, _translate("poseVideoClass", "30fps"))
        self.comboBox2.setItemText(1, _translate("poseVideoClass", "25fps"))
        self.comboBox2.setItemText(2, _translate("poseVideoClass", "20fps"))
        self.comboBox2.setItemText(3, _translate("poseVideoClass", "15fps"))
        self.comboBox2.setItemText(4, _translate("poseVideoClass", "10fps"))
        self.sendButton.setText(_translate("poseVideoClass", "send"))
        self.toolBar.setWindowTitle(_translate("poseVideoClass", "toolBar"))
        self.actionOpen.setText(_translate("poseVideoClass", "Open"))
