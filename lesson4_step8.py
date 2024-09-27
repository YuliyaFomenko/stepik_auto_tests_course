# Посчитать математическую функцию от x
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

try: 
    browser = webdriver.Chrome()
    # Открыть страницу
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )
    # Нажать на кнопку "Book"
    button1 = browser.find_element(By.CSS_SELECTOR, "button#book")
    button1.click()
    
    # Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
    # old Считать значение для переменной x
    x_element = browser.find_element(By.CSS_SELECTOR, "label #input_value")
    x = x_element.text
    y = calc(x)
    
    # old Ввести ответ в текстовое поле
    input1 = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input1.send_keys(y)
    
    # old Нажать на кнопку Submit
    button2 = browser.find_element(By.CSS_SELECTOR, "button#solve")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()