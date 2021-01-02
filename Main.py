# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 22:37:34 2021

@author: Hamza Laanani
"""

from selenium import webdriver

#Getting Chrome Webdriver
driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.basketball-reference.com/players/")

#Get links
alphabet_links = driver.find_elements_by_xpath('.//div[@id="div_alphabet"]//ul//li//a')


for link in alphabet_links:
    a_link = driver.find_element_by_link_text(link.text)
    a_link.click()
    
    #Getting all rows in the table
    rows = driver.find_elements_by_xpath('.//table[@id="players"]//tbody//tr')
    
    for row in rows:
        columns = row.find_elements_by_xpath('.//td')
        player_name = row.find_element_by_xpath('.//th')
        print('Player Name: ' + player_name.text)
        for column in columns:
                print(column.text)