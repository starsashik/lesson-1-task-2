import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.flag = False
        self.pushButton.clicked.connect(self.draw)

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw_fig()
            self.qp.end()

    def draw(self):
        self.flag = True
        self.update()

    def draw_fig(self):
        a1 = randint(1, 160)
        x = randint(1, 339)
        y = randint(1, 339)
        self.qp.setBrush(QColor(255, 211, 0))
        self.qp.drawEllipse(x, y, a1, a1)


def except_hook(cls, exception, traceback):
    sys.excepthook(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
