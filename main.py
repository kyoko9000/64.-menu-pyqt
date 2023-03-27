# ************************** man hinh loai 2 *************************
import sys

from PyQt5.QtCore import QTimer
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui1 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.a = 0
        self.time = QTimer(self)
        self.time.timeout.connect(self.pic_change)
        self.time.start(50)

    def pic_change(self):
        self.a += 1
        self.uic.frame.setStyleSheet(f"background-color: rgba(255, 255, 255, {self.a});")
        if self.a == 255:
            self.time.disconnect()
        print(self.a)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())