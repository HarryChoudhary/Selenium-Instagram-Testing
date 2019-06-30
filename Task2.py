
#----------------------------------IMPORT PACKAGES----------------------------------------------------------------------

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#--------------------------------------OPENING INSTAGRAM------------------------------------------------------------------
driver = webdriver.Firefox()
driver.get("https://www.instagram.com/accounts/login/")
wait = WebDriverWait(driver, 10)

#--------------------------------------------SIGN UP--------------------------------------------------------------------
driver.find_elements_by_name("Sign up")
time.sleep(1)
driver.find_element_by_name("username").send_keys("choudharyharish6861.hc@gmail.com")#ENTERING USERNAME
driver.find_element_by_name("password").send_keys("harish12345")#ENTERING PASSWORD

#-------------------CLICKING ON LOGIN BUTTON----------------------------------------------------------------------------
driver.find_element_by_xpath("//*[contains(text(), 'Log In')]").click()
time.sleep(5)

#-------------CLICKING ON NOTIFICATION  NOT NOW BUTTON------------------------------------------------------------------
driver.find_element_by_xpath("//*[contains(text(), 'Not Now')]").click()
time.sleep(1)

#----------------------OPENING EMMA WATSON ACCOUNT----------------------------------------------------------------------
name= driver.find_element_by_css_selector(".XTCLo").send_keys("emmawatson")
time.sleep(2)
#---------------------CLICK ON EMMA ACCOUNT-----------------------------------------------------------------------------
driver.find_element_by_xpath("//*[contains(text(), 'Emma Watson')]").click()
time.sleep(2)

#--------------------------CLICKING ON FOLLOWERS BUTTON-----------------------------------------------------------------
driver.find_element_by_css_selector("li.Y8-fY:nth-child(2) > a:nth-child(1)").click()
time.sleep(2)

#--------------------------FOR LOOP SELECTING 1 TO 100 FOLLOWERS--------------------------------------------------------
for i in range(1,101):
    wait = WebDriverWait(driver, 10)


#------TAKING THERE FOLLOWERS NUMBER CHECK VISIBILITY OF NAME [STR(I) ITERTING 1 TO 100]--------------------------------
#------FOLLOWERS NUMBER WILL START FROM 1 TO 100

    elm = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/ul/div/li["+str(i)+"]")))

#------TAKING THE NAME OF FOLLOWERS BY CLICKING ON HREF IT WILL SELECT THE INSTAGRAM ACCOUNT LINK ----------------------
    x1=driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/ul/div/li["+str(i)+"]")
    linkvalue = x1.find_element_by_tag_name("a").get_attribute("href")

#--------PRINTING NUMBERS AND HREF LINK OF FOLLOWERS FROM 1 TO 100------------------------------------------------------
    print("Follower Number" + str(i)+ ": " + linkvalue)

#------------DYNAMIC LOADING PAGE AND SCROLLONG  THE FOLLOWERS TILL I ==100---------------------------------------------

    driver.execute_script("arguments[0].scrollIntoView();", elm)

#-------------------SELECTING THE 100TH FOLLOWER OF EMMA WATSON AND CLICKING ON FOLLOW BUTTON---------------------------

driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/ul/div/li[100]/div/div[1]/div[2]/div[1]/a").click()
time.sleep(1)
driver.find_element_by_xpath("//*[contains(text(), 'Follow')]").click()

#-----------------SUCCESSFULLY PRINTING THE 100TH FOLLWER IS FOLLWED----------------------------------------------------
print("100th Name Followed is by link"+":"+"  "+ linkvalue )
