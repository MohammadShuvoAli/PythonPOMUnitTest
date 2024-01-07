import unittest
import HtmlTestRunner
from selenium import webdriver

import time
import sys
sys.path.append('C:\\Users\\Shuvo\\OneDrive - American International University-Bangladesh\\GitHub\\PythonPOMUnitTest')
from pageObjects.LoginPage import LoginPage

class LoginTest(unittest.TestCase):
    baseURL = "https://admin-demo.nopcommerce.com/"
    email = "admin@yourstore.com"
    password = "admin"
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_login(self):
        lp = LoginPage(self.driver)
        lp.setEmail(self.email)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(5)
        self.assertEqual("Dashboard / nopCommerce administration", self.driver.title, "Title did not match!!!")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\Shuvo\\OneDrive - American International University-Bangladesh\\GitHub\\PythonPOMUnitTest\\reports"))
