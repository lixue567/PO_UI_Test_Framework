import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.login_utils import logger
from common.base_page import BasePage
from common.element_data_utils import ElementdataUtils

class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        # self.username_inputbox = {'element_name':'用户名输入框',
        #                           'locator_type':'xpath',
        #                           'locator_value':'//input[@name="account"]',
        #                           'timeout': 5 }
        # self.password_inputbox = {'element_name': '密码输入框',
        #                           'locator_type': 'xpath',
        #                           'locator_value': '//input[@name="password"]',
        #                           'timeout': 4}
        # self.login_button = {'element_name': '登录按钮',
        #                           'locator_type': 'xpath',
        #                           'locator_value': '//button[@id="submit"]',
        #                           'timeout': 2}
        #加载所有元素的信息
        elements = ElementdataUtils('login_page').get_element_info()
        self.username_inputbox = elements['username_inputbox']
        self.password_inputbox = elements['password_inputbox']
        self.login_button = elements['login_button']

    # 方法 == 》控件的操作
    def input_username(self,username):
        self.input(self.username_inputbox, username)

    def input_password(self,password):
        self.input(self.password_inputbox, password)

    def click_login(self):
        self.click(self.login_button)

if __name__=="__main__":
    current_path = os.path.dirname(__file__)
    driver_path = os.path.join(current_path, '../webdriver/chromedriver')
    driver = webdriver.Chrome(executable_path=driver_path)
    login_page = LoginPage(driver)
    login_page.open_url('http://106.53.50.202:8999/zentao4/www/my/')
    login_page.input_username('lixue')
    login_page.input_password('lixue@123')
    login_page.click_login()


