from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://en-gb.facebook.com/reg/')

driver.find_element_by_name('firstname').send_keys('Azzin')
driver.find_element_by_name('lastname').send_keys('Maharil')

# Email and Confrim email
driver.find_element_by_name('reg_email__').send_keys('hello@world.com')
driver.find_element_by_name('reg_email_confirmation__').send_keys('hello@world.com')

#Password
driver.find_element_by_name('reg_passwd__').send_keys('testing@123')

# select date of birth
driver.find_element_by_id('day').send_keys('25')
driver.find_element_by_id('month').send_keys('Apr')
driver.find_element_by_id('year').send_keys('1999')

# select gender
driver.find_element_by_css_selector("input[name='sex'][value='2']").click()

# Click Register button
driver.find_element_by_name('websubmit').click()