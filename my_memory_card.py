from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
axe = QApplication([])
wind = QWidget()
wind.resize(400, 200)
wind.setWindowTitle('Memory Bohe')
wind.show()
axe.exec_()