#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

target = str(input('Enter name of person/group you want to target:'))

driver = webdriver.Firefox("/usr/local/bin/")
 
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
 
x_arg = '//span[contains(@title, '+ '"' +target + '"'+ ')]'

person_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))

person_title.click()



textget=driver.find_elements_by_class_name("selectable-text.invisible-space.copyable-text")
for Text in textget:
    print(Text.text)
while 1 :
	quit=input("Press Q|q for logout : ")
	if quit == 'Q' or quit == 'q':
		menu=driver.find_elements_by_class_name("rAUz7")
		menu[2].click()
		list=driver.find_elements_by_class_name("_10anr.vidHz._28zBA")
		list[5].click()
		break
