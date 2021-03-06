import unittest
from zipfile import ZipFile
import json
import os
import random
from time import sleep
from dateutil.parser import parse

from selenium.common.exceptions import NoSuchElementException

from appium import webdriver
import desired_capabilities

# the emulator is sometimes slow and needs time to think
SLEEPY_TIME = 3


class AppiumTests(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # def tearDown(self):
        # self.driver.quit()
        # self.driver.close()

    def test_extract_onix(self):

        # self.driver.tap([(955, 1190)])
        # # self.driver.get_screenshot_as_png()
        # sleep(SLEEPY_TIME)
        #
        # # 맘몬
        # self.driver.tap([(280, 389)])
        # sleep(5)
        #
        # # 프레이야
        # self.driver.tap([(215, 435)])
        # sleep(5)
        #
        # self.driver.tap([(175, 1355)])
        # self.driver.tap([(275, 1355)])
        # self.driver.tap([(375, 1355)])
        # self.driver.tap([(475, 1355)])
        # self.driver.tap([(575, 1355)])
        # self.driver.tap([(675, 1355)])
        # self.driver.tap([(775, 1355)])
        # sleep(4)
        #
        # self.driver.tap([(960, 455)])
        # sleep(SLEEPY_TIME)
        #
        # self.driver.tap([(555, 1200)])
        # sleep(SLEEPY_TIME)
        #
        # self.driver.tap([(960, 600)])
        # sleep(SLEEPY_TIME)
        while True:
            self.driver.tap([(940, 1435)]) # go affection
            sleep(1.05)

            self.driver.tap([(830, 820)]) # select D class
            sleep(1.05)
            self.driver.tap([(575, 1185)]) # start affection
            sleep(1.05)
            self.driver.tap([(540, 1500)]) # confirm
            sleep(1.05)

            self.driver.tap([(830, 820)]) # select C class
            sleep(1.05)
            self.driver.tap([(575, 1185)]) # start affection
            sleep(1.05)
            self.driver.tap([(540, 1500)]) # confirm
            sleep(1.05)

            self.driver.tap([(830, 820)]) # select B class
            sleep(1.05)
            self.driver.tap([(575, 1185)]) # start affection
            sleep(1.05)
            self.driver.tap([(540, 1500)]) # confirm
            sleep(1.05)

            self.driver.tap([(550, 375)]) # get reward
            sleep(1.05)
            self.driver.tap([(540, 1165)]) # confirm
            sleep(1.05)

            sleep(10)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AppiumTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
