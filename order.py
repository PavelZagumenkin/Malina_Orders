# Form implementation generated from reading ui file 'Order.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background: #fff")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, -20, 1281, 741))
        self.stackedWidget.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.stackedWidget.setAcceptDrops(False)
        self.stackedWidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.stackedWidget.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.stackedWidget.setLineWidth(1)
        self.stackedWidget.setMidLineWidth(0)
        self.stackedWidget.setObjectName("stackedWidget")
        self.p_home = QtWidgets.QWidget()
        self.p_home.setObjectName("p_home")
        self.autor_text = QtWidgets.QLabel(self.p_home)
        self.autor_text.setGeometry(QtCore.QRect(800, 669, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.autor_text.setFont(font)
        self.autor_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.autor_text.setObjectName("autor_text")
        self.logo_721 = QtWidgets.QLabel(self.p_home)
        self.logo_721.setGeometry(QtCore.QRect(-20, 20, 731, 721))
        self.logo_721.setText("")
        self.logo_721.setPixmap(QtGui.QPixmap("image/logo_721.png"))
        self.logo_721.setScaledContents(False)
        self.logo_721.setObjectName("logo_721")
        self.suppot_text = QtWidgets.QLabel(self.p_home)
        self.suppot_text.setGeometry(QtCore.QRect(810, 610, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.suppot_text.setFont(font)
        self.suppot_text.setMouseTracking(True)
        self.suppot_text.setTabletTracking(False)
        self.suppot_text.setAcceptDrops(False)
        self.suppot_text.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.suppot_text.setScaledContents(False)
        self.suppot_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.suppot_text.setWordWrap(True)
        self.suppot_text.setObjectName("suppot_text")
        self.btn_login = QtWidgets.QPushButton(self.p_home)
        self.btn_login.setGeometry(QtCore.QRect(800, 390, 351, 71))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.btn_login.setFont(font)
        self.btn_login.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.btn_login.setStyleSheet("QPushButton {\n"
"background-color: rgb(228, 107, 134);\n"
"border: none;\n"
"border-radius: 10px}\n"
"\n"
"QPushButton:hover {\n"
"border: 1px solid  rgb(0, 0, 0);\n"
"background-color: rgba(228, 107, 134, 0.9)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border:3px solid  rgb(0, 0, 0);\n"
"background-color: rgba(228, 107, 134, 1)\n"
"}")
        self.btn_login.setCheckable(False)
        self.btn_login.setObjectName("btn_login")
        self.line_password = QtWidgets.QLineEdit(self.p_home)
        self.line_password.setGeometry(QtCore.QRect(800, 290, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        self.line_password.setFont(font)
        self.line_password.setTabletTracking(False)
        self.line_password.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.line_password.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.line_password.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhHiddenText|QtCore.Qt.InputMethodHint.ImhNoAutoUppercase|QtCore.Qt.InputMethodHint.ImhNoPredictiveText|QtCore.Qt.InputMethodHint.ImhSensitiveData)
        self.line_password.setMaxLength(16)
        self.line_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.line_password.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.line_password.setObjectName("line_password")
        self.line_login = QtWidgets.QLineEdit(self.p_home)
        self.line_login.setGeometry(QtCore.QRect(800, 210, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        self.line_login.setFont(font)
        self.line_login.setTabletTracking(False)
        self.line_login.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.line_login.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.line_login.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.line_login.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.line_login.setMaxLength(24)
        self.line_login.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.line_login.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.line_login.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.LogicalMoveStyle)
        self.line_login.setClearButtonEnabled(False)
        self.line_login.setObjectName("line_login")
        self.label_login_password = QtWidgets.QLabel(self.p_home)
        self.label_login_password.setGeometry(QtCore.QRect(800, 170, 351, 20))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        self.label_login_password.setFont(font)
        self.label_login_password.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_login_password.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_login_password.setObjectName("label_login_password")
        self.line_login.raise_()
        self.line_password.raise_()
        self.autor_text.raise_()
        self.logo_721.raise_()
        self.suppot_text.raise_()
        self.btn_login.raise_()
        self.label_login_password.raise_()
        self.stackedWidget.addWidget(self.p_home)
        self.p_settings = QtWidgets.QWidget()
        self.p_settings.setEnabled(False)
        self.p_settings.setObjectName("p_settings")
        self.label_settings_title = QtWidgets.QLabel(self.p_settings)
        self.label_settings_title.setGeometry(QtCore.QRect(30, 50, 631, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(20)
        self.label_settings_title.setFont(font)
        self.label_settings_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_settings_title.setObjectName("label_settings_title")
        self.label_OLAP_P = QtWidgets.QLabel(self.p_settings)
        self.label_OLAP_P.setGeometry(QtCore.QRect(30, 120, 321, 21))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.label_OLAP_P.setFont(font)
        self.label_OLAP_P.setObjectName("label_OLAP_P")
        self.btn_path_OLAP_P = QtWidgets.QPushButton(self.p_settings)
        self.btn_path_OLAP_P.setGeometry(QtCore.QRect(750, 150, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.btn_path_OLAP_P.setFont(font)
        self.btn_path_OLAP_P.setStyleSheet("QPushButton {\n"
"background-color: rgb(228, 107, 134);\n"
"border: none;\n"
"border-radius: 10px}\n"
"\n"
"QPushButton:hover {\n"
"border: 1px solid  rgb(0, 0, 0);\n"
"background-color: rgba(228, 107, 134, 0.9)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border:3px solid  rgb(0, 0, 0);\n"
"background-color: rgba(228, 107, 134, 1)\n"
"}")
        self.btn_path_OLAP_P.setCheckable(False)
        self.btn_path_OLAP_P.setObjectName("btn_path_OLAP_P")
        self.btn_path_dayWeek_bakery = QtWidgets.QPushButton(self.p_settings)
        self.btn_path_dayWeek_bakery.setGeometry(QtCore.QRect(750, 250, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.btn_path_dayWeek_bakery.setFont(font)
        self.btn_path_dayWeek_bakery.setStyleSheet("QPushButton {\n"
"background-color: rgb(228, 107, 134);\n"
"border: none;\n"
"border-radius: 10px}\n"
"\n"
"QPushButton:hover {\n"
"border: 1px solid  rgb(0, 0, 0);\n"
"background-color: rgba(228, 107, 134, 0.9)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border:3px solid  rgb(0, 0, 0);\n"
"background-color: rgba(228, 107, 134, 1)\n"
"}")
        self.btn_path_dayWeek_bakery.setCheckable(False)
        self.btn_path_dayWeek_bakery.setObjectName("btn_path_dayWeek_bakery")
        self.label_OLAP_dayWeek_bakery = QtWidgets.QLabel(self.p_settings)
        self.label_OLAP_dayWeek_bakery.setGeometry(QtCore.QRect(30, 220, 511, 21))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.label_OLAP_dayWeek_bakery.setFont(font)
        self.label_OLAP_dayWeek_bakery.setObjectName("label_OLAP_dayWeek_bakery")
        self.btn_path_ost_cakes = QtWidgets.QPushButton(self.p_settings)
        self.btn_path_ost_cakes.setGeometry(QtCore.QRect(750, 550, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.btn_path_ost_cakes.setFont(font)
        self.btn_path_ost_cakes.setStyleSheet("QPushButton {\n"
"background-color: rgb(228, 107, 134);\n"
"border: none;\n"
"border-radius: 10px}\n"
"\n"
"QPushButton:hover {\n"
"border: 1px solid  rgb(0, 0, 0);\n"
"background-color: rgba(228, 107, 134, 0.9)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border:3px solid  rgb(0, 0, 0);\n"
"background-color: rgba(228, 107, 134, 1)\n"
"}")
        self.btn_path_ost_cakes.setCheckable(False)
        self.btn_path_ost_cakes.setObjectName("btn_path_ost_cakes")
        self.label_ost_cakes = QtWidgets.QLabel(self.p_settings)
        self.label_ost_cakes.setGeometry(QtCore.QRect(30, 520, 331, 21))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.label_ost_cakes.setFont(font)
        self.label_ost_cakes.setObjectName("label_ost_cakes")
        self.btn_pie = QtWidgets.QPushButton(self.p_settings)
        self.btn_pie.setGeometry(QtCore.QRect(870, 180, 351, 71))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.btn_pie.setFont(font)
        self.btn_pie.setStyleSheet("QPushButton {\n"
"background-color: rgb(228, 107, 134);\n"
"border: none;\n"
"border-radius: 10px}\n"
"\n"
"QPushButton:hover {\n"
"border: 1px solid  rgb(0, 0, 0);\n"
"background-color: rgba(228, 107, 134, 0.9)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border:3px solid  rgb(0, 0, 0);\n"
"background-color: rgba(228, 107, 134, 1)\n"
"}")
        self.btn_pie.setCheckable(False)
        self.btn_pie.setObjectName("btn_pie")
        self.btn_cakes = QtWidgets.QPushButton(self.p_settings)
        self.btn_cakes.setGeometry(QtCore.QRect(870, 290, 351, 71))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.btn_cakes.setFont(font)
        self.btn_cakes.setStyleSheet("QPushButton {\n"
"background-color: rgb(228, 107, 134);\n"
"border: none;\n"
"border-radius: 10px}\n"
"\n"
"QPushButton:hover {\n"
"border: 1px solid  rgb(0, 0, 0);\n"
"background-color: rgba(228, 107, 134, 0.9)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border:3px solid  rgb(0, 0, 0);\n"
"background-color: rgba(228, 107, 134, 1)\n"
"}")
        self.btn_cakes.setCheckable(False)
        self.btn_cakes.setObjectName("btn_cakes")
        self.btn_others = QtWidgets.QPushButton(self.p_settings)
        self.btn_others.setGeometry(QtCore.QRect(870, 510, 351, 71))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.btn_others.setFont(font)
        self.btn_others.setStyleSheet("QPushButton {\n"
"background-color: rgb(228, 107, 134);\n"
"border: none;\n"
"border-radius: 10px}\n"
"\n"
"QPushButton:hover {\n"
"border: 1px solid  rgb(0, 0, 0);\n"
"background-color: rgba(228, 107, 134, 0.9)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border:3px solid  rgb(0, 0, 0);\n"
"background-color: rgba(228, 107, 134, 1)\n"
"}")
        self.btn_others.setCheckable(False)
        self.btn_others.setObjectName("btn_others")
        self.btn_bakery = QtWidgets.QPushButton(self.p_settings)
        self.btn_bakery.setGeometry(QtCore.QRect(870, 70, 351, 71))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.btn_bakery.setFont(font)
        self.btn_bakery.setStyleSheet("QPushButton {\n"
"background-color: rgb(228, 107, 134);\n"
"border: none;\n"
"border-radius: 10px}\n"
"\n"
"QPushButton:hover {\n"
"border: 1px solid  rgb(0, 0, 0);\n"
"background-color: rgba(228, 107, 134, 0.9)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border:3px solid  rgb(0, 0, 0);\n"
"background-color: rgba(228, 107, 134, 1)\n"
"}")
        self.btn_bakery.setCheckable(False)
        self.btn_bakery.setObjectName("btn_bakery")
        self.btn_filling = QtWidgets.QPushButton(self.p_settings)
        self.btn_filling.setGeometry(QtCore.QRect(870, 400, 351, 71))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.btn_filling.setFont(font)
        self.btn_filling.setStyleSheet("QPushButton {\n"
"background-color: rgb(228, 107, 134);\n"
"border: none;\n"
"border-radius: 10px}\n"
"\n"
"QPushButton:hover {\n"
"border: 1px solid  rgb(0, 0, 0);\n"
"background-color: rgba(228, 107, 134, 0.9)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border:3px solid  rgb(0, 0, 0);\n"
"background-color: rgba(228, 107, 134, 1)\n"
"}")
        self.btn_filling.setCheckable(False)
        self.btn_filling.setObjectName("btn_filling")
        self.btn_path_dayWeek_pie = QtWidgets.QPushButton(self.p_settings)
        self.btn_path_dayWeek_pie.setGeometry(QtCore.QRect(750, 350, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.btn_path_dayWeek_pie.setFont(font)
        self.btn_path_dayWeek_pie.setStyleSheet("QPushButton {\n"
"background-color: rgb(228, 107, 134);\n"
"border: none;\n"
"border-radius: 10px}\n"
"\n"
"QPushButton:hover {\n"
"border: 1px solid  rgb(0, 0, 0);\n"
"background-color: rgba(228, 107, 134, 0.9)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border:3px solid  rgb(0, 0, 0);\n"
"background-color: rgba(228, 107, 134, 1)\n"
"}")
        self.btn_path_dayWeek_pie.setCheckable(False)
        self.btn_path_dayWeek_pie.setObjectName("btn_path_dayWeek_pie")
        self.label_OLAP_dayWeek_pie = QtWidgets.QLabel(self.p_settings)
        self.label_OLAP_dayWeek_pie.setGeometry(QtCore.QRect(30, 320, 531, 21))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.label_OLAP_dayWeek_pie.setFont(font)
        self.label_OLAP_dayWeek_pie.setObjectName("label_OLAP_dayWeek_pie")
        self.btn_path_dayWeek_cakes = QtWidgets.QPushButton(self.p_settings)
        self.btn_path_dayWeek_cakes.setGeometry(QtCore.QRect(750, 450, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.btn_path_dayWeek_cakes.setFont(font)
        self.btn_path_dayWeek_cakes.setStyleSheet("QPushButton {\n"
"background-color: rgb(228, 107, 134);\n"
"border: none;\n"
"border-radius: 10px}\n"
"\n"
"QPushButton:hover {\n"
"border: 1px solid  rgb(0, 0, 0);\n"
"background-color: rgba(228, 107, 134, 0.9)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border:3px solid  rgb(0, 0, 0);\n"
"background-color: rgba(228, 107, 134, 1)\n"
"}")
        self.btn_path_dayWeek_cakes.setCheckable(False)
        self.btn_path_dayWeek_cakes.setObjectName("btn_path_dayWeek_cakes")
        self.label_OLAP_dayWeek_cakes = QtWidgets.QLabel(self.p_settings)
        self.label_OLAP_dayWeek_cakes.setGeometry(QtCore.QRect(30, 420, 521, 21))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.label_OLAP_dayWeek_cakes.setFont(font)
        self.label_OLAP_dayWeek_cakes.setObjectName("label_OLAP_dayWeek_cakes")
        self.btn_path_ost_filling = QtWidgets.QPushButton(self.p_settings)
        self.btn_path_ost_filling.setGeometry(QtCore.QRect(750, 650, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.btn_path_ost_filling.setFont(font)
        self.btn_path_ost_filling.setStyleSheet("QPushButton {\n"
"background-color: rgb(228, 107, 134);\n"
"border: none;\n"
"border-radius: 10px}\n"
"\n"
"QPushButton:hover {\n"
"border: 1px solid  rgb(0, 0, 0);\n"
"background-color: rgba(228, 107, 134, 0.9)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border:3px solid  rgb(0, 0, 0);\n"
"background-color: rgba(228, 107, 134, 1)\n"
"}")
        self.btn_path_ost_filling.setCheckable(False)
        self.btn_path_ost_filling.setObjectName("btn_path_ost_filling")
        self.label_ost_filling = QtWidgets.QLabel(self.p_settings)
        self.label_ost_filling.setGeometry(QtCore.QRect(30, 620, 351, 21))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.label_ost_filling.setFont(font)
        self.label_ost_filling.setObjectName("label_ost_filling")
        self.btn_exit = QtWidgets.QPushButton(self.p_settings)
        self.btn_exit.setGeometry(QtCore.QRect(870, 620, 351, 71))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.btn_exit.setFont(font)
        self.btn_exit.setStyleSheet("QPushButton {\n"
"background-color: rgb(228, 107, 134);\n"
"border: none;\n"
"border-radius: 10px}\n"
"\n"
"QPushButton:hover {\n"
"border: 1px solid  rgb(0, 0, 0);\n"
"background-color: rgba(228, 107, 134, 0.9)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border:3px solid  rgb(0, 0, 0);\n"
"background-color: rgba(228, 107, 134, 1)\n"
"}")
        self.btn_exit.setCheckable(False)
        self.btn_exit.setObjectName("btn_exit")
        self.lineEdit_OLAP_P = QtWidgets.QLineEdit(self.p_settings)
        self.lineEdit_OLAP_P.setEnabled(False)
        self.lineEdit_OLAP_P.setGeometry(QtCore.QRect(30, 150, 691, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        self.lineEdit_OLAP_P.setFont(font)
        self.lineEdit_OLAP_P.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.lineEdit_OLAP_P.setStyleSheet("padding-left: 5px")
        self.lineEdit_OLAP_P.setObjectName("lineEdit_OLAP_P")
        self.lineEdit_OLAP_dayWeek_bakery = QtWidgets.QLineEdit(self.p_settings)
        self.lineEdit_OLAP_dayWeek_bakery.setEnabled(False)
        self.lineEdit_OLAP_dayWeek_bakery.setGeometry(QtCore.QRect(30, 250, 691, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        self.lineEdit_OLAP_dayWeek_bakery.setFont(font)
        self.lineEdit_OLAP_dayWeek_bakery.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.lineEdit_OLAP_dayWeek_bakery.setStyleSheet("padding-left: 5px")
        self.lineEdit_OLAP_dayWeek_bakery.setObjectName("lineEdit_OLAP_dayWeek_bakery")
        self.lineEdit_OLAP_dayWeek_pie = QtWidgets.QLineEdit(self.p_settings)
        self.lineEdit_OLAP_dayWeek_pie.setEnabled(False)
        self.lineEdit_OLAP_dayWeek_pie.setGeometry(QtCore.QRect(30, 350, 691, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        self.lineEdit_OLAP_dayWeek_pie.setFont(font)
        self.lineEdit_OLAP_dayWeek_pie.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.lineEdit_OLAP_dayWeek_pie.setStyleSheet("padding-left: 5px")
        self.lineEdit_OLAP_dayWeek_pie.setObjectName("lineEdit_OLAP_dayWeek_pie")
        self.lineEdit_OLAP_dayWeek_cakes = QtWidgets.QLineEdit(self.p_settings)
        self.lineEdit_OLAP_dayWeek_cakes.setEnabled(False)
        self.lineEdit_OLAP_dayWeek_cakes.setGeometry(QtCore.QRect(30, 450, 691, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        self.lineEdit_OLAP_dayWeek_cakes.setFont(font)
        self.lineEdit_OLAP_dayWeek_cakes.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.lineEdit_OLAP_dayWeek_cakes.setStyleSheet("padding-left: 5px")
        self.lineEdit_OLAP_dayWeek_cakes.setObjectName("lineEdit_OLAP_dayWeek_cakes")
        self.lineEdit_ost_filling = QtWidgets.QLineEdit(self.p_settings)
        self.lineEdit_ost_filling.setEnabled(False)
        self.lineEdit_ost_filling.setGeometry(QtCore.QRect(30, 650, 691, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        self.lineEdit_ost_filling.setFont(font)
        self.lineEdit_ost_filling.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.lineEdit_ost_filling.setStyleSheet("padding-left: 5px")
        self.lineEdit_ost_filling.setObjectName("lineEdit_ost_filling")
        self.lineEdit_ost_cakes = QtWidgets.QLineEdit(self.p_settings)
        self.lineEdit_ost_cakes.setEnabled(False)
        self.lineEdit_ost_cakes.setGeometry(QtCore.QRect(30, 550, 691, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        self.lineEdit_ost_cakes.setFont(font)
        self.lineEdit_ost_cakes.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.lineEdit_ost_cakes.setStyleSheet("padding-left: 5px")
        self.lineEdit_ost_cakes.setObjectName("lineEdit_ost_cakes")
        self.stackedWidget.addWidget(self.p_settings)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.line_login, self.line_password)
        MainWindow.setTabOrder(self.line_password, self.btn_path_dayWeek_bakery)
        MainWindow.setTabOrder(self.btn_path_dayWeek_bakery, self.btn_path_OLAP_P)
        MainWindow.setTabOrder(self.btn_path_OLAP_P, self.btn_path_ost_cakes)
        MainWindow.setTabOrder(self.btn_path_ost_cakes, self.btn_pie)
        MainWindow.setTabOrder(self.btn_pie, self.btn_cakes)
        MainWindow.setTabOrder(self.btn_cakes, self.btn_others)
        MainWindow.setTabOrder(self.btn_others, self.btn_bakery)
        MainWindow.setTabOrder(self.btn_bakery, self.btn_filling)
        MainWindow.setTabOrder(self.btn_filling, self.btn_path_dayWeek_pie)
        MainWindow.setTabOrder(self.btn_path_dayWeek_pie, self.btn_path_dayWeek_cakes)
        MainWindow.setTabOrder(self.btn_path_dayWeek_cakes, self.btn_path_ost_filling)
        MainWindow.setTabOrder(self.btn_path_ost_filling, self.btn_exit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Малина 64"))
        self.autor_text.setText(_translate("MainWindow", "Автор логиcтических расчетов Китов А.О. \n"
" Разработчик Загуменкин П.И."))
        self.suppot_text.setText(_translate("MainWindow", "По всем вопросам работы программы \n"
" обращаться в Отдел построения"))
        self.btn_login.setText(_translate("MainWindow", "Начать работу"))
        self.line_password.setPlaceholderText(_translate("MainWindow", "Пароль"))
        self.line_login.setPlaceholderText(_translate("MainWindow", "Логин"))
        self.label_login_password.setText(_translate("MainWindow", "Введите логин и пароль"))
        self.label_settings_title.setText(_translate("MainWindow", "Настройка подключения внешних данных"))
        self.label_OLAP_P.setText(_translate("MainWindow", "Укажите путь к OLAP отчету по продажам"))
        self.btn_path_OLAP_P.setText(_translate("MainWindow", "..."))
        self.btn_path_dayWeek_bakery.setText(_translate("MainWindow", "..."))
        self.label_OLAP_dayWeek_bakery.setText(_translate("MainWindow", "Укажите путь к OLAP отчету по продажам по дням недели - выпечка"))
        self.btn_path_ost_cakes.setText(_translate("MainWindow", "..."))
        self.label_ost_cakes.setText(_translate("MainWindow", "Укажите путь к Остаткам по складам - торты"))
        self.btn_pie.setText(_translate("MainWindow", "ПИРОЖНЫЕ"))
        self.btn_cakes.setText(_translate("MainWindow", "ТОРТЫ"))
        self.btn_others.setText(_translate("MainWindow", "ОСТАЛЬНОЕ"))
        self.btn_bakery.setText(_translate("MainWindow", "ВЫПЕЧКА"))
        self.btn_filling.setText(_translate("MainWindow", "НАЧИНКИ"))
        self.btn_path_dayWeek_pie.setText(_translate("MainWindow", "..."))
        self.label_OLAP_dayWeek_pie.setText(_translate("MainWindow", "Укажите путь к OLAP отчету по продажам по дням недели - пирожные"))
        self.btn_path_dayWeek_cakes.setText(_translate("MainWindow", "..."))
        self.label_OLAP_dayWeek_cakes.setText(_translate("MainWindow", "Укажите путь к OLAP отчету по продажам по дням недели - торты"))
        self.btn_path_ost_filling.setText(_translate("MainWindow", "..."))
        self.label_ost_filling.setText(_translate("MainWindow", "Укажите путь к Остаткам по складам - начинка"))
        self.btn_exit.setText(_translate("MainWindow", "ВЫХОД"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())