from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstaBot():
    def __init__(self, username, password):
        self.username=username
        self.password=password
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instagram.com/")



        time.sleep(2)

        login_user=self.driver.find_element_by_xpath("//input[@name= 'username']")
        login_pass =self.driver.find_element_by_xpath("//input[@name='password']")
        login_user.clear()
        login_pass.clear()
        login_user.send_keys(self.username)
        login_pass.send_keys(self.password)
        submit=self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        not_now=self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
        time.sleep(2)
        not_now2=self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
        time.sleep(2)
        click_user=self.driver.find_element_by_xpath("//a[contains(text(),'testerfake1')]").click()
        time.sleep(2)
        following=self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
        time.sleep(2)
        sugs=self.driver.find_element_by_xpath("//h4[contains(text(), 'Suggestions For You')]")
        self.driver.execute_script('arguments[0].scrollIntoView()',sugs)
        time.sleep(2)
        links=self.driver.find_elements_by_tag_name("a")
        names=[name.text for name in links if name.text != " "]
        print(names)
        time.sleep(2)
        close=self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button").click()



        while (True):
            pass

InstaBot('username','password')