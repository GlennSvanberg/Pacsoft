import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
#import io
#import requests

# Read customer
columns = ['customer_name', 'address', 'postal_code', 'city', 'phone']
#url = 'https://suite.mobilegroup.se/pacsoft.csv'
url = 'http://suite.mobilegroup.se/pacsoft.csv'
#s = requests.get(url).content
#df = pd.read_csv(io.StringIO(s.decode('utf-8')), names=columns)
df = pd.read_csv(url, names=columns)
customer = df.loc[0]

# open Pacsoft
# Optional argument, if not specified will search path.
driver = webdriver.Chrome("chromedriver.exe")
driver.get('http://www.pacsoftonline.se')

# login
driver.switch_to_frame("outer")
driver.find_element_by_name('CompanyLogin').send_keys("password")
driver.find_element_by_name('UserPass').send_keys("username")
driver.find_element_by_name("act_LoginActions_Login").click()

# Standardutskrift
driver.switch_to_frame("menu")
driver.find_element_by_link_text('Standardutskrift').click()

# Ny
driver.switch_to.default_content()
driver.switch_to_frame("outer")
driver.switch_to_frame("body")
driver.find_element_by_name(
    "act_ShipmentJobEdit1Actions2_RECEIVEREditRadioBtn").click()
time.sleep(1)


# name
driver.find_element_by_name('RECEIVERName').send_keys(customer.customer_name)
# Addressrad 1
driver.find_element_by_name(
    'RECEIVERDeliveryAddress1').send_keys(customer.address)
# Postnummer
driver.find_element_by_name('RECEIVERDeliveryZipcode').send_keys(
    str(customer.postal_code))
# Postnummer
driver.find_element_by_name('RECEIVERDeliveryCity').send_keys(customer.city)
# Kontakt
driver.find_element_by_name(
    'RECEIVERContact').send_keys(customer.customer_name)
# Telefon
driver.find_element_by_name('RECEIVERPhone').send_keys(
    "0" + str(customer.phone))
# SMS Nummer
driver.find_element_by_name('RECEIVERSms').send_keys("0" + str(customer.phone))

# time.sleep(5) # Let the user actually see something!
# driver.quit()
'''
ids = driver.find_elements_by_xpath('//*[@id]')
for ii in ids:
    print (ii.get_attribute('id'))



ids = driver.find_elements_by_xpath('//*[@id]')
for ii in ids:
    print (ii.get_attribute('id'))
'''
