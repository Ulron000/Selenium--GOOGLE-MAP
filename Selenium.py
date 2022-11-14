import selenium

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 

driver=webdriver.Chrome("C:\\Users\\Yuvra\\OneDrive\\python\\chromedriver")
driver.get("https://www.google.com/maps/@19.1135744,72.876032,12z")

time.sleep(2)

   #searchplace
searchboxinput="Shree Dwarkadhish Temple, Dwarka, Gujarat"
place=driver.find_element("id","searchboxinput")
place.send_keys(searchboxinput)
place.send_keys(Keys.ENTER)
    
    #layers
time.sleep(5)
Layers=driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[23]/div[5]/div/div[2]/button").click()

   #directions
time.sleep(5)
directions=driver.find_element(By.CLASS_NAME,"EgL07d").click()

   #find
time.sleep(6)
find=driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input")
find.send_keys("Dombivali")
time.sleep(5)
search=driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]").click()

   #Yourlocation
time.sleep(5)
yourlocation=driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[23]/div[1]/div[3]/div[5]/div/button").click()

   #Gas
time.sleep(5)
gas=driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[5]/div/div/div/div[1]/div/div/div/div/div[5]/div[2]/div[2]/div/button").click()
time.sleep(5)
search=driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[3]/div/a").click()
 
  #Share
time.sleep(3)
share=driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[4]/div[5]/button").click()

  #Embed a map
time.sleep(3)
embedmap=driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div/div[2]/div/div[3]/div/div/div[1]/div[2]/button[2]").click()
