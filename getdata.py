from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv


employee_file = open('employee_file.csv', mode='a', newline='')
employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)



driver = webdriver.Firefox()
file1 = open('websites', 'r')
Lines = file1.readlines()
c=1
##driver = webdriver.Firefox()
# Strips the newline character
while (c==1):
	for line in Lines:
		print( line.strip())
		driver.get(line.strip())
		element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "5 Dakika")))
		element.click()
		namemy= driver.find_element_by_xpath(("//h1[@itemprop='name']")).text
		table = driver.find_element_by_xpath(("//table[@class='genTbl closedTbl crossRatesTbl']")).text
		table2 = driver.find_element_by_xpath(("//table[@class='genTbl closedTbl technicalIndicatorsTbl smallTbl float_lang_base_1']")).text
		table3 = driver.find_element_by_xpath(("//table[@class='genTbl closedTbl movingAvgsTbl float_lang_base_2']")).text
		table4 = driver.find_element_by_xpath(("//div[@class='top bold inlineblock']")).text
		employee_writer.writerow([table, table2, table3])
		print(namemy+"\n")
	pass
	file1 = open('myfile.txt', 'r')
	Lines = file1.readlines()




