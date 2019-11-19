from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QBrush, QPainter, QColor
import sys
from random import randint
from UI import Ui_MainWindow


class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.d = False
        self.setupUi(self)
        self.pushButton.clicked.connect(self.draw)
    
    def draw(self):
        self.d = True
        self.update()

    def paintEvent(self, event):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        self.qp = QPainter()
        self.qp.begin(self)
        self.qp.setPen(QColor(r, g, b))
        self.drawCircle()
        self.qp.end()

    def drawCircle(self):
        if self.d:
            a = randint(0, 100)
            self.qp.drawEllipse(self.pushButton.x(), self.pushButton.y() + self.pushButton.height(), a, a)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ap = App()
    ap.show()
    sys.exit(app.exec_())
