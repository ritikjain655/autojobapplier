from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


import time
myemail="myemail"
mypassword="mypass"
chrome_driver_path="/Users/ritikjain/Downloads/chromedriver-mac-x64/chromedriver"
driver=webdriver.Chrome(service=ChromeService(chrome_driver_path))
driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3959204476&f_AL=true&f_E=2&f_WT=1%2C3%2C2&geoId=102713980&keywords=software%20engineer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true')
#time.sleep(2)

signin_button=driver.find_element(By.LINK_TEXT, "Sign in")

#time.sleep(2)
signin_button.click()
email_box=driver.find_element(By.ID, "username")
email_box.click()
email_box.send_keys(myemail)
#time.sleep(2)

password_box=driver.find_element(By.ID, "password")
password_box.click()
password_box.send_keys(mypassword)
#time.sleep(2)

password_box.send_keys(Keys.ENTER)
#time.sleep(5)
all_listed_jobs = driver.find_elements(By.CSS_SELECTOR,".job-card-container--clickable")
#time.sleep(3)


for jobs in all_listed_jobs:
    jobs.click()
    time.sleep(1)
    apply_button=driver.find_element(By.CSS_SELECTOR,".jobs-s-apply button")
    apply_button.click()
    time.sleep(1)
    next_button=driver.find_element(By.CSS_SELECTOR,"footer button")

    next_button.click()
    next_button2=driver.find_element(By.CLASS_NAME,"artdeco-button--primary")
    next_button2.click()

    next_button3 = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
    next_button3.click()
    #time.sleep(1)

    additional=driver.find_element(By.XPATH,"//*[@id='radio-button-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3906517701-120779995-multipleChoice']/div[1]/label")
    additional.click()

    review=driver.find_element(By.CLASS_NAME,"artdeco-button--primary")
    review.click()
    submitbutton=driver.find_element(By.CLASS_NAME,"artdeco-button--primary")
    submitbutton.click()
    time.sleep(5)
    break

#time.sleep(5)
