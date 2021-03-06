import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QGroupBox, QVBoxLayout, QHBoxLayout, QRadioButton, QLabel

class MainWindow(QDialog):

    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Radio Button"
        self.top = 400
        self.left = 200
        self.width = 400
        self.height = 150
        self.icon_name = "images/home.png"

        self._init_window()

    def _init_window(self):
        self.setWindowIcon(QtGui.QIcon(self.icon_name))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self._create_ui_components()
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.group_box)

        self.lbl_Info = QLabel(self)
        self.lbl_Info.setFont(QtGui.QFont("Sanserif", 15))
        vbox.addWidget(self.lbl_Info)
        
        self.setLayout(vbox)
        
        self.show()

    def _create_ui_components(self):
        self.group_box = QGroupBox("What is your favorite sport?")
        self.group_box.setFont(QtGui.QFont("Sanserif", 13))
        
        hbox_layout = QHBoxLayout()

        self.rdbtn_soccer = QRadioButton("Soccer")
        self.rdbtn_soccer.setIcon(QtGui.QIcon("images/soccer.png"))
        self.rdbtn_soccer.setIconSize(QtCore.QSize(30, 30))
        self.rdbtn_soccer.setFont(QtGui.QFont("Sanserif", 13))
        self.rdbtn_soccer.toggled.connect(self._on_radiobutton_checked)
        hbox_layout.addWidget(self.rdbtn_soccer)

        self.rdbtn_basketball = QRadioButton("Basketball")
        self.rdbtn_basketball.setIcon(QtGui.QIcon("images/basketball.png"))
        self.rdbtn_basketball.setIconSize(QtCore.QSize(30, 30))
        self.rdbtn_basketball.setFont(QtGui.QFont("Sanserif", 13))
        self.rdbtn_basketball.toggled.connect(self._on_radiobutton_checked)
        hbox_layout.addWidget(self.rdbtn_basketball)

        self.rdbtn_tennis = QRadioButton("Tennis")
        self.rdbtn_tennis.setIcon(QtGui.QIcon("images/tennis.png"))
        self.rdbtn_tennis.setIconSize(QtCore.QSize(30, 30))
        self.rdbtn_tennis.setFont(QtGui.QFont("Sanserif", 13))
        self.rdbtn_tennis.toggled.connect(self._on_radiobutton_checked)
        hbox_layout.addWidget(self.rdbtn_tennis)
        
        self.group_box.setLayout(hbox_layout)

    def _on_radiobutton_checked(self):
        rdbtn = self.sender()
        if rdbtn.isChecked():
            self.lbl_Info.setText(f"Sport selected: {rdbtn.text()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())