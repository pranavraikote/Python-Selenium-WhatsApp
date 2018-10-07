#Import the modules
from selenium import webdriver
import time
import sys

#Exception handling block
try:
    print('Establishing connection')
    
    #Start the webdriver and connect to the website
    driver=webdriver.Chrome("C:\\Users\\Pranav\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://web.whatsapp.com/")
    driver.maximize_window()
    print('Please scan the Whatsapp QR Code')        
    time.sleep(10)
    
except:
    print('Error in establishing driver connection')    
    driver.quit()
    print('Connection was closed')
    sys.exit()

#Find the conversation of the required contact
print('Finding the user')

user=driver.find_element_by_xpath('//span[@title="***Contact Name***"]') #Replace user name in the [@title=""]
if user is None:
    print('User not found. Exiting program')    
    driver.quit()
    print('Connection was closed')
    sys.exit()
else:
    user.click()
    print('User found')

#Find the text box and send the message
text=driver.find_element_by_class_name('_2S1VP')
text.send_keys('This message was sent by an automated script !                         Finally it worked !')
print('Message Typed')
time.sleep(3)

#Click the send button
send=driver.find_element_by_class_name('_35EW6')
send.click()
print('Message sent')
time.sleep(5)

#Click on options menu for log-out
print('Logging Out')
log=driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]')
log.click()
time.sleep(3)

#Find the log-out option and click it
out=driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/span/div/ul/li[6]/div')
out.click()
time.sleep(2)

print('Log out successfull')

#Close the webdriver session
driver.quit()
print('Connection was closed')
