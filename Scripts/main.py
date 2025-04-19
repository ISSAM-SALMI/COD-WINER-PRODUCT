from scraper.scraper import Scraper
from dotenv import load_dotenv
import os
import csv
from openpyxl import Workbook
load_dotenv()



scraper = Scraper()
scraper.open_page(os.getenv("LINK1"))
scraper.SaisirInfo()
scraper.Clik_Button()
for i in range(1,int(os.getenv("USAN"))+1) :
    link = os.getenv("USA") + str(i)
    links = scraper.getListOfProducts_per_country(link)
    for link in links :
        data = scraper.getDetailsOfProduct(link)
        scraper.save_product_data(data)
        print(data)
