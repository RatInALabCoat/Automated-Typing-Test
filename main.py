from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.typing.com/student/tests")
driver.implicitly_wait(5)

start_test_button = driver.find_element("xpath", "(//a[contains(@href,'1-minute')])[1]").click()
driver.implicitly_wait(5)

continue_button = driver.find_element("xpath", "//button[contains(text(),'Continue')]").click()
driver.implicitly_wait(6)

actions = ActionChains(driver)
all_letter = driver.find_elements("xpath", "//div[contains(@class,'letter')]")

for letter in all_letter:
    send_letter = letter.text
    print(send_letter)
    actions.key_down(send_letter).perform()
    
else:
    sleep(5)
    driver.close()
