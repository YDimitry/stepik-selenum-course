from math import log, sin

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

calc = lambda x: log(abs(12*sin(x)))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    book = browser.find_element_by_id('book')

    price = WebDriverWait(browser, 15).until(
        ec.text_to_be_present_in_element((By.ID,'price'), '$100')
    )
    book.click()
    solve = browser.find_element_by_id('solve')
    answer = browser.find_element_by_id('answer')
    x = browser.find_element_by_id('input_value')
    answer.send_keys(str(calc(int(x.text))))
    solve.click()

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()

finally:
    browser.quit()