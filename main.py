
import sys
from bs4 import BeautifulSoup
import requests
from PyQt5.QtWidgets import QListWidget

from PyQt5.uic import loadUi

from PyQt5.QtWidgets import QApplication,QDialog,QWidget,QStackedWidget,QFileDialog
from PyQt5.QtGui import QIcon

class exhange(QDialog):
    def __init__(self):
        super(QDialog,self).__init__()
        loadUi(r"C:\Users\bugra\OneDrive\Masaüstü\ımdb-list\ımdb.ui",self)

        self.baglan()

    def baglan(self):



        url = "https://www.imdb.com/chart/top/"
        response = requests.get(url)
        html = response.content

        soup = BeautifulSoup(html, "html.parser")  # attrs attribute
        top_250 = soup.find("tbody", attrs={"class": "lister-list"}).find_all("tr")
        basla = 1
        for film in top_250:  # gelenler önce find sonra ifadeler direkt yazılır
            name = film.find("td", attrs={"class": "titleColumn"}).a.text
            year = film.find("td", {"class": "titleColumn"}).span.text
            imdb = film.find("td", {"class": "ratingColumn imdbRating"}).strong.text
            community = film.find("td", {"class": "ratingColumn imdbRating"}).strong.get(
                "title")  # direkt title get ile çekildi..
            self.listWidget.insertItem(basla,"{}.\nFilm ismi :{}\nFilm yılı :{}\nFilm imdb :{}\n\n{}".format(basla, name, year, imdb, community))

            basla += 1

            if basla > 100:
                break




app = QApplication(sys.argv)
ana = exhange()
widget = QStackedWidget()
widget.addWidget(ana)
widget.setWindowTitle("ımdb ilk 100")
widget.setWindowIcon(QIcon(r"C:\Users\bugra\OneDrive\Masaüstü\döviz-program\imdb.png"))
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("çıkılıyor")