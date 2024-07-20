from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.speedtest.net/")

time.sleep(2)
cookies = driver.find_element(By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
cookies.click()

GO_button = driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
GO_button.click()

download_speed = driver.find_element(By.XPATH,
                                     value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]'
                                           '/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
update_speed = driver.find_element(By.XPATH,
                                     value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]'
                                           '/div/div/div[2]/div[1]/div[2]/div/div[2]/span')

time.sleep(40)
if float(download_speed.text) < 500 * 0.7:
    print(f"It is slow, {download_speed.text}")
else:
    print(f"It's good, {download_speed.text}")
if float(update_speed.text) < 200:
    print(f"It won't update till the next year, {update_speed.text}")
else:
    print(f"It's good, {update_speed.text}")

driver.quit()
