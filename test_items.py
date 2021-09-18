import time

import pytest
from selenium import webdriver


def test_add_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.maximize_window()
    basket = browser.find_element_by_css_selector("#add_to_basket_form>.btn")
    assert basket.is_displayed(), "The 'Add_to_basket' button is not presented"
  
