from selenium import webdriver
from bs4 import BeautifulSoup as bs
from datetime import datetime as dt
from datetime import timedelta as td
import os


chrome_options_1= webdriver.ChromeOptions()
chrome_options_1.add_argument("user-data-dir=D:\\Anuraj\\selenium profile\\Profile 1")
driver = webdriver.Chrome(options=chrome_options_1)

chrome_options_2= webdriver.ChromeOptions()
chrome_options_2.add_argument("user-data-dir=D:\\Anuraj\\selenium profile\\Meet")
meet = webdriver.Chrome(options=chrome_options_2)

driver.get("https://web.whatsapp.com/")



#path = "//span[contains(text(),'CSE B.Tech 2022 Passout')]"
#path = "//div[@class='_3Tw1q']//span[@class='_1hI5g _1XH7x _1VzZY'][contains(text(),'CSE B.Tech 2022 Passout')]"

'''Choose the Group'''

choose = input("Choose your group , then press any key");

driver.implicitly_wait(20)
#driver.find_element_by_xpath(path).click()
#driver.implicitly_wait(5)

def getlink():
    try:
        html = driver.page_source
        soup = bs(html, 'html.parser')
        links = soup.find_all('a')
        link = links[len(links) - 1].text
        return link
    except:
        return "No"

def gettime():
    now = dt.now()
    time = now.strftime("%H:%M")
    return time


def addtime():
    time = dt.now() + td(minutes=1)
    time = time.strftime("%H:%M")
    return time

def meetClass(link):

    meet.get(link)
    # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='IYwVEf HotEze uB7U9e nAZzG']//div[@class='oTVIqe BcUQQ']//*[local-name()='svg']"))).click()
    # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='IYwVEf HotEze nAZzG']//div[@class='oTVIqe BcUQQ']//*[local-name()='svg'] "))).click()
    # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Ask to join')]"))).click()
    meet.implicitly_wait(10)
    try:
        meet.find_element_by_xpath("/html[1]/body[1]/div[1]/c-wiz[1]/div[1]/div[1]/div[8]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
        meet.find_element_by_xpath(
            "//body/div[@id='yDmH0d']/c-wiz[1]/div[1]/div[1]/div[8]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]").click()
        meet.find_element_by_xpath(
            "//body/div[@id='yDmH0d']/c-wiz[1]/div[1]/div[1]/div[8]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]").click()

        meet.find_element_by_xpath("//span[contains(text(),'Ask to join')]").click()

    except:
        meet.find_element_by_xpath("//div[contains(text(),'Ready to join?')]").click()
        meet.find_element_by_xpath(
            "//body/div[@id='yDmH0d']/c-wiz[1]/div[1]/div[1]/div[8]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]").click()
        meet.find_element_by_xpath(
            "//body/div[@id='yDmH0d']/c-wiz[1]/div[1]/div[1]/div[8]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]").click()

        meet.find_element_by_xpath("//span[contains(text(), 'Join now')]").click()

    try:
        meet.find_element_by_xpath(
            "//body/div[@id='yDmH0d']/c-wiz[1]/div[1]/div[1]/div[8]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]").click()
        meet.find_element_by_xpath(
            "//body/div[@id='yDmH0d']/c-wiz[1]/div[1]/div[1]/div[8]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]").click()
    except:
        pass

def meet_close():
    try:
        data = meet.page_source
        soup = bs(data, 'html.parser')
        participants = soup.find("span", attrs={'class' :"wnPUne N0PJ8e"}).text
        participants = int(participants)
        if(participants < 2):
            meet.find_element_by_xpath("/html[1]/body[1]/div[1]/c-wiz[1]/div[1]/div[1]/div[8]/div[3]/div[9]/div[2]/div[2]/div[1]/span[1]/span[1]/*[local-name()='svg'][1]").click()
            return True
    except:
        return False



checktime = gettime()
if os.path.isfile('class_link.txt'):
    with open ('class_link.txt', 'r') as f:
        checklink = f.read()
        print(checklink)
meet_end = 1

while True:
    time = gettime()
    if time == checktime:
        link = getlink()
        print(gettime()+" : "+link)
        checktime = addtime()
        if link != checklink and link != 'No' and meet_end == 1:
            checklink = link

            with open("class_link.txt", "w+") as f:
                f.write(checklink)
            f.close()

            if "meet.google.com" in link:
                meet_end = 0
                meetClass(link)

        else:
            print("No link")

    if meet_close():
        meet_end = 1


