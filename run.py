#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Hamdi
from selenium import webdriver



option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(options=option)
driver.get('https://www.taobao.com/')
driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])

driver.find_element_by_id('TPL_username_1').send_keys('账号')
driver.find_element_by_name('TPL_password').send_keys('密码')
