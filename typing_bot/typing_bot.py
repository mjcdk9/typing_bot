import time
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui as py


path = "chromedriver.exe"
driver = webdriver.Chrome(path)
url = 'https://www.livechat.com/typing-speed-test/#/'
driver.get(url)
textBoxXpath = '//*[@id="app"]/div/div[2]/div[1]/div/span/div[2]/span/div/div[2]/div[1]'
textBox = driver.find_element(By.XPATH, textBoxXpath)
textBox.click()
time.sleep(5)
i = 1
wordXpath = f"//*[@id='app']/div/div[2]/div[1]/div/span/div[2]/span/div/div[2]/div[2]/span[{i}]"

firstWord = driver.find_element(By.XPATH, wordXpath).text

py.write(firstWord)



def typeBot():
    timerXpath = '//*[@id="app"]/div/div[2]/div[1]/div/span/div[1]/div/div[1]/div/div[1]'
    i=1
    while True:
        time = driver.find_element(By.XPATH, timerXpath).text
        print(time)
        i = i+1

        if time == "00":
            break
        else:

            if i == 6:
                i = 1
            else:
                continue

            wordXpath = f"//*[@id='app']/div/div[2]/div[1]/div/span/div[2]/span/div/div[2]/div[2]/span[{i}]"
            firstWord = driver.find_element(By.XPATH, wordXpath).text

            py.write(firstWord + " ")


for _ in range(5):
    x = threading.Thread(target=typeBot)
    x.start()

print("done")