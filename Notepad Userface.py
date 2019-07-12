import sys

import os #dosya açma işlemleri için

from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QHBoxLayout,QVBoxLayout,QFileDialog #dosya açma ve kaydetme işlemlerinde

from PyQt5.QtWidgets import QAction,qApp,QMainWindow

class Notepad(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.yazı_alanı=QTextEdit()
        self.temizle=QPushButton("Temizle")
        self.ac=QPushButton("Aç")
        self.kaydet=QPushButton("Kaydet")
        self.setGeometry(100,100,500,500)

        h_box=QHBoxLayout()

        h_box.addWidget(self.temizle)
        h_box.addWidget(self.ac)
        h_box.addWidget(self.kaydet)

        v_box=QVBoxLayout()

        v_box.addWidget(self.yazı_alanı)

        v_box.addLayout(h_box)

        self.setLayout(v_box)

        self.setWindowTitle("NOTEPAD")

        self.temizle.clicked.connect(self.yaziyi_temizle)
        self.ac.clicked.connect(self.dosya_ac)
        self.kaydet.clicked.connect(self.dosyayi_kaydet)



    def yaziyi_temizle(self):
        self.yazı_alanı.clear()

    def dosya_ac(self):
        dosya_ismi=QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("Desktop"))
        with open(dosya_ismi[0],"r") as file:
            self.yazı_alanı.setText(file.read())

    def dosyayi_kaydet(self):
        dosya_ismi=QFileDialog.getOpenFileName(self,"Dosya Kaydet",os.getenv("Desktop"))
        with open(dosya_ismi[0],"w") as file:
            file.write(self.yazı_alanı.toPlainText()) #toPlain text alanındaki bütün yazıları alır




class Menu(QMainWindow):

    def __init__(self):

        super().__init__()

        self.pencere=Notepad()

        self.setCentralWidget(self.pencere)

        self.menuleri_olustur()


    def menuleri_olustur(self):

        menubar=self.menuBar()

        dosya=menubar.addMenu("Dosya")

        dosya_ac=QAction("Dosya Aç",self)
        dosya_ac.setShortcut("Ctrl+O")

        dosya_kaydet=QAction("Dosya Kaydet",self)
        dosya_kaydet.setShortcut("Ctrl+S")

        dosya_temizle=QAction("Dosya Temizle",self)
        dosya_temizle.setShortcut("Ctrl+D")

        dosya_cikis=QAction("Çıkış",self)
        dosya_cikis.setShortcut("Ctrl+E")

        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(dosya_cikis)
        dosya.addAction(dosya_temizle)

        dosya.triggered.connect(self.response)

        self.setWindowTitle("NOTEPAD")

        self.show()

    def response(self,action):

        if action.text()=="Dosya Aç":
            self.pencere.dosya_ac()

        elif action.text()=="Dosya Kaydet":
            self.pencere.dosyayi_kaydet()

        elif action.text()=="Dosya Temizle":
            self.pencere.yaziyi_temizle()
        elif action.text()=="Çıkış":
            qApp.quit()












app=QApplication(sys.argv)

menu=Menu()

sys.exit(app.exec_())