import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service() # é usada para instanciar chrome webdriver
options = webdriver.ChromeOptions() # definir preferencias do chrome
driver = webdriver.Chrome(service=service, options=options)

url = "https://www.youtube.com"

driver.get(url)
time.sleep(2)
driver.find_element(By.TAG_NAME, value="input").send_keys("blockkstar")
driver.find_element(By.TAG_NAME, value="input").send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element(By.LINK_TEXT, value="LH CHUCRO - BROTOU UMA P!RANHA [prod. Neckklace] (Oficial Video)").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, value="ytp-fullscreen-button").send_keys(Keys.ENTER)
time.sleep(200)
