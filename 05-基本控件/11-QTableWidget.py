"""
表格控件
"""
import random
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidget, QHBoxLayout, QVBoxLayout, QPushButton, QFrame, \
    QTableWidgetItem


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.table = None
        self.setWindowTitle('QTableWidget')
        self.init_ui()

    def init_ui(self):
        self.table = QTableWidget(self)
        font = QFont('微软雅黑')
        font.setBold(True)
        font.setPointSize(16)
        # 给 table head 设置字体
        self.table.horizontalHeader().setFont(font)

        self.table.setFrameShape(QFrame.NoFrame) ## 无边框表格
        self.table.horizontalHeader().setFixedHeight(50) ## 表头高度固定 50

        self.table.setColumnCount(5) ## 设置表格一共有 5列
        self.table.setHorizontalHeaderLabels(['id', "姓名", "年龄", '学号', '地址']) # 设置表头文字

        self.table.horizontalHeader().setSectionsClickable(False) #表头禁止点击
        self.table.horizontalHeader().setStyleSheet('QHeaderView::section{background:green}') #　设置表头为绿色




        main_layout = QHBoxLayout()
        button_group_layout = QVBoxLayout()
        button_group_layout.setAlignment(Qt.AlignTop)

        add_row_btn = QPushButton('增加一行')
        add_row_btn.clicked.connect(self.add_row)
        delete_row_btn = QPushButton('减少一行')
        delete_row_btn.clicked.connect(self.delete_row)
        editable_row_btn = QPushButton('可以编辑')
        choose_row_btn = QPushButton('选择整行')

        button_group_layout.addWidget(add_row_btn)
        button_group_layout.addWidget(delete_row_btn)
        button_group_layout.addWidget(editable_row_btn)
        button_group_layout.addWidget(choose_row_btn)
        main_layout.addWidget(self.table)
        main_layout.addLayout(button_group_layout)

        self.setLayout(main_layout)

    def add_row(self):
        self.row_count = self.table.rowCount() # 获取当前总行，用作删除一行使用
        print(self.row_count)
        self.table.setItem(self.row_count, 0, QTableWidgetItem("1"))
        self.table.setItem(self.row_count, 1, QTableWidgetItem('张三'))
        self.table.setItem(self.row_count, 2, QTableWidgetItem(25))
        self.table.setItem(self.row_count, 3, QTableWidgetItem(11111))
        self.table.setItem(self.row_count, 4, QTableWidgetItem("湖北荆州"))
        self.row_count += 1
        self.table.setRowCount(self.row_count)

    def delete_row(self):
        print(self.row_count)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()