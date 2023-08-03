from utils import *
from locators.element_locators import ElementLocators
import time

driver = driver_setup()

driver.get("https://www.google.com/recaptcha/api2/demo")

driver.switch_to.frame(try_getting(ElementLocators.RECAPTCHA_IFRAME, driver))
try_getting(ElementLocators.RECAPTCHA_CHECKBOX, driver).click()
print("Switching...")
driver.switch_to.default_content
driver.switch_to.frame(try_getting("body > div:nth-child(2) > div:nth-child(2) > iframe", driver))
print("Success")

time.sleep(10000)
