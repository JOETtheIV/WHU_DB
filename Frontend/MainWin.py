# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWin(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet("QWidget#Form{\n"
"background:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(254, 234, 255, 255), stop:0.664773 rgba(155, 190, 235, 255), stop:1 rgba(245, 226, 223, 255));}\n"
"")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet("QFrame#frame{\n"
"border-radius:20px;\n"
"background:rgba(255,255,255,100)}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(9)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(9)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(9)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(9)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.horizontalLayout.addWidget(self.frame_3)
        spacerItem1 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 4)
        self.horizontalLayout_7.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "系统入口"))
        self.label.setText(_translate("Form", "欢迎使用WHU图书管理系统"))
        self.pushButton_7.setText(_translate("Form", "读者入口"))
        self.pushButton_6.setText(_translate("Form", "管理员入口"))
        self.pushButton_5.setText(_translate("Form", "超级管理员入口"))
        self.pushButton_4.setText(_translate("Form", "退出"))

