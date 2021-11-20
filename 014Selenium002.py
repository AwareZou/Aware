from selenium import webdriver
from time import sleep

wd=webdriver.Chrome(r'c:\chromedriver.exe')
##wd.get('https://www.12306.cn/index/')
wd.get('http://mealorderdev.we-linkin.com:6605/login')

userId='weizou'
password='Pe212101'
sleep(1)
wd.find_elements_by_class_name('ant-input')[0].send_keys(userId)
wd.find_elements_by_class_name('ant-input')[1].send_keys(password)
login=wd.find_element_by_class_name('styles_loginBtn__aOa2R').click()
# user.send_keys(userId)
# pw.send_keys(password)
# login.click()

sleep(1)
wd.switch_to.window(wd.window_handles[0])
sleep(1)
wd.find_element_by_xpath('//*[@id="root"]/div/div/div/button').click()
# submit.click()


