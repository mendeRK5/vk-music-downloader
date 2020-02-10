# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/audio.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(780, 522)
        MainWindow.setMinimumSize(QtCore.QSize(780, 522))
        MainWindow.setMaximumSize(QtCore.QSize(780, 522))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.login = QtWidgets.QLineEdit(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(440, 10, 181, 31))
        self.login.setObjectName("login")
        self.login_text = QtWidgets.QLabel(self.centralwidget)
        self.login_text.setGeometry(QtCore.QRect(140, 10, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.login_text.setFont(font)
        self.login_text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.login_text.setObjectName("login_text")
        self.password_text = QtWidgets.QLabel(self.centralwidget)
        self.password_text.setGeometry(QtCore.QRect(370, 50, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.password_text.setFont(font)
        self.password_text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.password_text.setObjectName("password_text")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(440, 50, 181, 31))
        self.password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.password.setInputMask("")
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setDragEnabled(False)
        self.password.setObjectName("password")
        self.link_text = QtWidgets.QLabel(self.centralwidget)
        self.link_text.setGeometry(QtCore.QRect(10, 90, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.link_text.setFont(font)
        self.link_text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.link_text.setObjectName("link_text")
        self.user_link = QtWidgets.QLineEdit(self.centralwidget)
        self.user_link.setGeometry(QtCore.QRect(440, 90, 181, 31))
        self.user_link.setObjectName("user_link")
        self.btnConfirm = QtWidgets.QPushButton(self.centralwidget)
        self.btnConfirm.setGeometry(QtCore.QRect(590, 420, 181, 29))
        self.btnConfirm.setAutoDefault(False)
        self.btnConfirm.setDefault(False)
        self.btnConfirm.setObjectName("btnConfirm")
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        self.status_label.setGeometry(QtCore.QRect(10, 120, 68, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.status_label.setFont(font)
        self.status_label.setObjectName("status_label")
        self.saveData = QtWidgets.QCheckBox(self.centralwidget)
        self.saveData.setEnabled(True)
        self.saveData.setGeometry(QtCore.QRect(630, 90, 111, 27))
        self.saveData.setObjectName("saveData")
        self.statusInfo = QtWidgets.QLabel(self.centralwidget)
        self.statusInfo.setGeometry(QtCore.QRect(70, 130, 701, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.statusInfo.setFont(font)
        self.statusInfo.setWordWrap(True)
        self.statusInfo.setObjectName("statusInfo")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(10, 165, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(False)
        self.progressBar.setGeometry(QtCore.QRect(610, 172, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.progressBar.setFont(font)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(1)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.progress_label = QtWidgets.QLabel(self.centralwidget)
        self.progress_label.setEnabled(False)
        self.progress_label.setGeometry(QtCore.QRect(470, 170, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.progress_label.setFont(font)
        self.progress_label.setObjectName("progress_label")
        self.trackList = QtWidgets.QTreeWidget(self.centralwidget)
        self.trackList.setEnabled(False)
        self.trackList.setGeometry(QtCore.QRect(10, 200, 761, 211))
        self.trackList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.trackList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.trackList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.trackList.setObjectName("trackList")
        self.trackList.header().setVisible(False)
        self.search = QtWidgets.QLineEdit(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(10, 420, 151, 20))
        self.search.setObjectName("search")
        self.volumeSlider = QtWidgets.QSlider(self.centralwidget)
        self.volumeSlider.setGeometry(QtCore.QRect(170, 421, 160, 19))
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setSliderPosition(100)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.volumeSlider.setTickInterval(10)
        self.volumeSlider.setObjectName("volumeSlider")
        self.pause_button = QtWidgets.QPushButton(self.centralwidget)
        self.pause_button.setGeometry(QtCore.QRect(340, 415, 31, 31))
        self.pause_button.setStyleSheet("border-radius:15px;image:url(:/images/pause_button.png);")
        self.pause_button.setText("")
        self.pause_button.setObjectName("pause_button")
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setGeometry(QtCore.QRect(380, 415, 31, 31))
        self.stop_button.setStyleSheet("border-radius:15px;image:url(:/images/stop_button.png);")
        self.stop_button.setText("")
        self.stop_button.setObjectName("stop_button")
        self.play_status = QtWidgets.QSlider(self.centralwidget)
        self.play_status.setGeometry(QtCore.QRect(10, 450, 761, 19))
        self.play_status.setMaximum(100)
        self.play_status.setOrientation(QtCore.Qt.Horizontal)
        self.play_status.setObjectName("play_status")
        self.sort_tracks = QtWidgets.QCheckBox(self.centralwidget)
        self.sort_tracks.setGeometry(QtCore.QRect(630, 120, 111, 31))
        self.sort_tracks.setObjectName("sort_tracks")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 780, 30))
        self.menuBar.setObjectName("menuBar")
        self.music_menu = QtWidgets.QMenu(self.menuBar)
        self.music_menu.setObjectName("music_menu")
        self.help_menu = QtWidgets.QMenu(self.menuBar)
        self.help_menu.setObjectName("help_menu")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.saveAll = QtWidgets.QAction(MainWindow)
        self.saveAll.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/save_all.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveAll.setIcon(icon1)
        self.saveAll.setObjectName("saveAll")
        self.saveWithoutLinks = QtWidgets.QAction(MainWindow)
        self.saveWithoutLinks.setEnabled(False)
        self.saveWithoutLinks.setObjectName("saveWithoutLinks")
        self.downloadAllTracks = QtWidgets.QAction(MainWindow)
        self.downloadAllTracks.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/download_all.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.downloadAllTracks.setIcon(icon2)
        self.downloadAllTracks.setObjectName("downloadAllTracks")
        self.luckyMe = QtWidgets.QAction(MainWindow)
        self.luckyMe.setEnabled(False)
        self.luckyMe.setObjectName("luckyMe")
        self.exit = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit.setIcon(icon3)
        self.exit.setObjectName("exit")
        self.helpDialog = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpDialog.setIcon(icon4)
        self.helpDialog.setObjectName("helpDialog")
        self.aboutDialog = QtWidgets.QAction(MainWindow)
        self.aboutDialog.setObjectName("aboutDialog")
        self.music_menu.addAction(self.saveAll)
        self.music_menu.addAction(self.saveWithoutLinks)
        self.music_menu.addSeparator()
        self.music_menu.addAction(self.downloadAllTracks)
        self.music_menu.addSeparator()
        self.music_menu.addAction(self.luckyMe)
        self.music_menu.addSeparator()
        self.music_menu.addAction(self.exit)
        self.help_menu.addAction(self.helpDialog)
        self.help_menu.addSeparator()
        self.help_menu.addAction(self.aboutDialog)
        self.menuBar.addAction(self.music_menu.menuAction())
        self.menuBar.addAction(self.help_menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VKMusic Downloader"))
        self.login_text.setText(_translate("MainWindow", "Номер телефона или электронная почта:"))
        self.password_text.setText(_translate("MainWindow", "Пароль:"))
        self.link_text.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10.5pt;\">Ссылка на профиль (пост, альбом) пользователя (сообщества):</span></p></body></html>"))
        self.btnConfirm.setToolTip(_translate("MainWindow", "Получить список аудиозаписей пользователя"))
        self.btnConfirm.setText(_translate("MainWindow", "Получить аудиозаписи"))
        self.status_label.setText(_translate("MainWindow", "Статус:"))
        self.saveData.setToolTip(_translate("MainWindow", "Сохранить введенные данные?"))
        self.saveData.setText(_translate("MainWindow", "Запомнить"))
        self.statusInfo.setText(_translate("MainWindow", "Готов к работе."))
        self.label_4.setText(_translate("MainWindow", "Список аудиозаписей:"))
        self.progressBar.setFormat(_translate("MainWindow", "Скачано %v из %m"))
        self.progress_label.setText(_translate("MainWindow", "Прогресс скачивания:"))
        self.trackList.headerItem().setText(0, _translate("MainWindow", "Аудиозаписи"))
        self.search.setPlaceholderText(_translate("MainWindow", "Поиск..."))
        self.sort_tracks.setToolTip(_translate("MainWindow", "Упорядочить список в алфавитном порядке по имени исполнителя?"))
        self.sort_tracks.setText(_translate("MainWindow", "Сортировать"))
        self.music_menu.setTitle(_translate("MainWindow", "&Музыка"))
        self.help_menu.setTitle(_translate("MainWindow", "&Помощь"))
        self.saveAll.setText(_translate("MainWindow", "&Сохранить"))
        self.saveAll.setStatusTip(_translate("MainWindow", "Сохранить список аудиозаписей в файл со ссылками для их скачивания"))
        self.saveAll.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.saveWithoutLinks.setText(_translate("MainWindow", "Сохранить &без ссылок"))
        self.saveWithoutLinks.setStatusTip(_translate("MainWindow", "Сохранить список аудиозаписей в файл без ссылок для их скачивания"))
        self.saveWithoutLinks.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.downloadAllTracks.setText(_translate("MainWindow", "С&качать всё"))
        self.downloadAllTracks.setStatusTip(_translate("MainWindow", "Скачать все аудиозаписи пользователя"))
        self.downloadAllTracks.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.luckyMe.setText(_translate("MainWindow", "&Мне повезёт"))
        self.luckyMe.setStatusTip(_translate("MainWindow", "Воспроизвести случайную аудиозапись из списка"))
        self.luckyMe.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.exit.setText(_translate("MainWindow", "&Выход"))
        self.exit.setStatusTip(_translate("MainWindow", "Выход из VKMusic Downloader"))
        self.exit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.helpDialog.setText(_translate("MainWindow", "&Помощь"))
        self.helpDialog.setStatusTip(_translate("MainWindow", "Помощь по VkMusic Downloader"))
        self.helpDialog.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.aboutDialog.setText(_translate("MainWindow", "&О программе"))
        self.aboutDialog.setStatusTip(_translate("MainWindow", "Информация о VkMusic Downloader"))
from gui import audio_res
