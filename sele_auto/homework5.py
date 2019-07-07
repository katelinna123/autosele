import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import  sleep


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://39.104.14.232/ecshop/wwwroot/admin/index.php')
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_class_name("button2").click()
sleep(2)
driver.switch_to.frame("menu-frame")
driver.find_element_by_xpath("//*[@id=\"menu-ul\"]/li/ul/li[1]/a").click()
driver.find_element_by_xpath("//*[@id=\"02_cat_and_goods\"]/ul/li[1]/a").click()

driver.switch_to.parent_frame()
driver.switch_to.frame("main_frame")
driver.find_element_by_xpath("/html/body/h1/span[1]/a").click()

driver.find_element_by_name("goods_name").send_keys(u"小霸王")

driver.find_element_by_xpath("//*[@id=\"cat_name\"]").click()
driver.find_element_by_xpath("//*[@id=\"treeDemo_cat_id_1_span\"]").click()

Select(driver.find_element_by_xpath("//*[@id=\"general-table\"]/tbody/tr[4]/td[2]/select").click()).select_by_index(3)
driver.find_element_by_xpath("//*[@id=\"brand_search\"]").send_keys(u"迪士尼")
driver.find_element_by_xpath("//*[@id=\"dishini迪士尼\"]/a").click()

Select(driver.find_element_by_xpath("//*[@id=\"suppliers_id\"]")).select_by_value(u"颐和果园")

driver.find_element_by_xpath("//*[@id=\"general-table\"]/tbody/tr[7]/td[2]/input[1]").send_keys("12")

driver.find_element_by_xpath("//*[@id=\"general-table\"]/tbody/tr[13]/td[2]/input").send_keys("3")

driver.find_element_by_xpath("//*[@id=\"promote_1\"]").send_keys("2")

file = "E:\\0e32c5ce641fa64fc29c9098b6c74f42.jpg"
driver.get(file)

driver.find_element_by_xpath("//*[@id=\"general-table\"]/tbody/tr[19]/td[2]/input[1]").send_keys("E:\\0e32c5ce641fa64fc29c9098b6c74f42.jpg")

driver.find_element_by_xpath("//*[@id=\"goods_info_submit\"]").click()
sleep(2)










driver.close()