# Filename: v_layout.py

import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('QHBoxLayout')
layout = QVBoxLayout()
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Center'))
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()

sys.exit(app.exec_())