from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *




class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #navBar
        navbar =QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('{<-}', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('{->}',self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload',self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        bing_btn = QAction('bing',self)
        bing_btn.triggered.connect(self.navigate_bing)
        navbar.addAction(bing_btn)

        google_btn = QAction('google', self)
        google_btn.triggered.connect(self.navigate_google)
        navbar.addAction(google_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)


        self.browser.urlChanged.connect(self.update_url)

    def navigate_bing(self):
        self.browser.setUrl(QUrl('http://bing.com'))

    def navigate_google(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):
        url =self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, url):
        self.url_bar.setText(url.toString())



app =QApplication(sys.argv)
QApplication.setApplicationName('Imperial')
window = MainWindow()
app.exec()