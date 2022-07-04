from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys # webdriver로 작동할 키 모듈
import time

# ChromeDriver로 접속
# 자신의 크롬 버전과 일치하는 webdriver 다운 받을 것
driver = webdriver.Chrome("C:/Users/USER/chromedriver_win32/chromedriver.exe")
# 로딩시간 3초
driver.implicitly_wait(3) 

driver.get("https://www.mangoplate.com/top_lists")


popup = driver.find_element_by_xpath("//*[@id='ad']/div/button[2]").click()
time.sleep(5)

# # top_lists 페이지 열기
# def initpage():
#     driver.get("https://www.mangoplate.com/top_lists")

# # base url + url
# def connect(url):
#     driver.get("https://www.mangoplate.com/"+url)

# class Toplist:
#     def __init__(self):
#         initpage()
    
#     def more(self):
#         while(1):
#             # 더보기 버튼 클릭
#             driver.find_element_by_xpath("//a[@class='btn-more']").click()

#     def tagClick(self, tag):
#         # 상단 태그 클릭
#         # #전체 버튼을 제외한 나머지 버튼 클릭
#         driver.find_element_by_xpath("//button[@data-keyword='"+tag+"']").send_keys(Keys.ENTER)

