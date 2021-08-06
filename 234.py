#! /usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import math
import os
import os.path

try:

# Открытие ссылки в браузере Хром
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

# Кликаем кнопку
    button = browser.find_element_by_class_name('btn-primary')
    button.click()

# Подтверждение алерта
    confirm = browser.switch_to.alert
    confirm.accept()

# Математика
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

# Находим число X на странице
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

# Вводим значение в строку ввода
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)


# Находим и кликаем кнопку Submit
    button = browser.find_element_by_class_name('btn-primary')
    button.click()


finally:
    time.sleep(10)
    browser.quit()

