import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
import codecs
import requests
from bs4 import BeautifulSoup as bf
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def messeg_stop(send, text):
    session.method('messages.send', {'user_id': send, 'message': text, 'random_id':get_random_id()})

def messeg(send, message1, promo):
    session.method('messages.send', {'user_id': send, 'message': message1, 'random_id':get_random_id()})
    for x in promo:
        session.method('messages.send', {'user_id': send, 'message': x, 'random_id':get_random_id()})

url = 'https://genshin.mihoyo.com/m/ru/news'
url_promo = 'http://guidesgame.ru/cheats/genshin-impact-kody-nabora/'

session=vk_api.VkApi(token='61bedcbf827b21e531d9474f808c8902536153bdd74d17424489e865c661e92f02188bd42c762222fff9f')
longpool =VkLongPoll(session)

while True:
    try:
        take_from = requests.get(url_promo)
        content =bf(take_from.text, 'lxml')

        a=0
        promo=[]
        while a<15: 
            a=a+1
            cod=content.find('tr', class_='row-'+str(a))
            try:
                if cod.find("em")==None:
                    promo_text=cod.find('strong').text
                    promo_text2=cod.find(class_='column-2').text
                    promo.append(promo_text)
                    promo.append(promo_text2)
                else:
                    promo_text=cod.find('strong').text
                    promo_text2=cod.find(class_='column-2').text
                    promo_text3=cod.find("em").text
                    promo.append(promo_text)
                    promo.append(promo_text2)
                    promo.append(promo_text3)
            except:
                pass

        chrome_options = Options()  
        chrome_options.add_argument("--headless")  
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C:\Users\Asus-Pro-Gaming\Desktop\Genshiprog\python\chromedriver.exe')
        driver.get(url)
        try:
            title=driver.find_element_by_partial_link_text('обыт').text
        except:
            title='Нету информации о событиях'
        try:
            for event in longpool.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                    reseived_message= event.text
                    sender=event.user_id
                    if 1==1:
                        messeg(sender, title, promo)
        except:
            pass
    except:
        messeg_stop(sender, 'Напишите через 1 минуту')