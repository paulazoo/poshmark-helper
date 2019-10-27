'''
If you add a bunch more items to your closet plz tell me bc rn
there isnt any scroll in ur closet but i can add if u need it

now let's make some bread and get rid of that student debt!
'''

#selenium
from selenium import webdriver
#keyboard manipulation
from selenium.webdriver.common.keys import Keys
#folder manipulation
import os
#keep track of time
import time
#sound notifications (beeps)
import winsound


#class to hold bot functions
class Poshmark:

    def __init__(self, username, password):
        #class gets username and password as attributes
        self.username = username
        self.password = password

    def newdriver(self):
        #open webdriver chrome browser
        self.driver = webdriver.Chrome('./chromedriver.exe')
    
    #logging in
    def login(self):
        #get poshmark login page
        self.driver.get('https://poshmark.com/login')
        #wait to load
        time.sleep(2)
        #find username box and password box by name attribute (from inspect element)
        #then send keys from self.username, self.password
        self.driver.find_element_by_name('login_form[username_email]').send_keys(self.username)
        self.driver.find_element_by_name('login_form[password]').send_keys(self.password)
        #find and click login button as first element with text "Log In" in div (insepct element)
        #self.driver.find_elements_by_xpath("//div[contains(text(), 'Log In')]")[0].click()
        self.driver.find_element_by_xpath("//button[@class='btn blue btn-primary']").click()
        #time to load
        time.sleep(2)
        print('logged in')
        
        time.sleep(10)
        
    
    def shareown(self, nstart, nend):
        #go to own closet and load
        self.driver.get('https://poshmark.com/closet/lilymalo')
        time.sleep(2)
        #set initial scroll height
        height = int(4000)
        #scroll
        self.driver.execute_script("window.scrollTo(0," + str(height) + ");")
        #open new window tab (for the pic links)
        self.driver.execute_script("window.open()")
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(3)
        #find clothes pics
        pics = self.driver.find_elements_by_class_name('covershot-con') 
        #number of pics found check
        print(len(pics)) #28
        if (nend>len(pics)):
            nend = len(pics)
        #find href links for all clothes
        pic_hrefs = [elem.get_attribute('href') for elem in pics]
        #ok time to share a bunch
        for i in range(nstart,nend):
            print(i)
            #switch new tab
            self.driver.switch_to.window(self.driver.window_handles[1])
            #go href pic link
            self.driver.get(pic_hrefs[i])
            time.sleep(15)
            #try to click share button
            try:
                self.driver.find_element_by_class_name('share').click()
                print('sharing!')
                self.driver.find_element_by_class_name('pm-followers-share-link').click()
                print('shared')
                time.sleep(3)
            except Exception as e:
                print(e)
                time.sleep(1)
            #back to original feed tab
            self.driver.switch_to.window(self.driver.window_handles[0])
        #after sharing all of your own then close extra window
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.close()
        
    #sharing community clothes feed function in hopes they'll share back
    #let's share a bunch of stuffffs
    def sharecom(self,npics):
        start=time.time()
        #go to feed url and load
        self.driver.get('https://poshmark.com/feed')
        #initial height
        print("hi1")
        height = int(2000)
        print("hi2")
        #open new tab for clothes
        self.driver.execute_script("window.open()")
        self.driver.switch_to.window(self.driver.window_handles[0])
        print("hi3")
        #loop for as many pics as needed
        for i in range(0,npics):
            print(i)
            time.sleep(3)
            height=int(height + (1000)) #scroll down height of about 1 pic
            self.driver.execute_script("window.scrollTo(0," + str(height) + ");")
            time.sleep(3) 
            #get general div of feed summaries
            feedsumdiv = self.driver.find_elements_by_xpath("//div[@class='feed__summary']")
            #print length check
            print(len(feedsumdiv))
            #find actual clickable pic elements
            pic = feedsumdiv[i].find_element_by_xpath(".//a[@data-et-name='feed_unit']")
            #find href links for all pics
            pic_href = pic.get_attribute('href')
            #href check
            print(str(pic_href))
            #not gonna share entire closets
            #can add brands or users to not share in here as well
            if "closet" in pic_href:
                print('not a listing')
            else:
                #switch new tab
                self.driver.switch_to.window(self.driver.window_handles[1])
                #go href pic link
                self.driver.get(pic_href)
                time.sleep(2)
                #try to click share button
                try:
                    self.driver.find_element_by_class_name('share').click()
                    print('sharing!')
                    self.driver.find_element_by_class_name('pm-followers-share-link').click()
                    print('shared')
                    time.sleep(3)
                except Exception as e:
                    print(e)
                    time.sleep(1)
                #back to original feed tab
                self.driver.switch_to.window(self.driver.window_handles[0])
            #after sharing then close extra window
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.close()
            end = time.time()
            print(end - start)
            freq = 2500  #2500 Hz
            duration = 1000  #1000 ms == 1 s
            winsound.Beep(freq, duration)
            time.sleep(0.5)
            winsound.Beep(freq, duration)
            time.sleep(0.5)
            winsound.Beep(freq, duration)
        


if __name__ == '__main__':
    #class instance for setting username, password
    pbpy = Poshmark('username','password')

    #actual actions
    
    #driver
    pbpy.newdriver()
    
    #login
    pbpy.login()
    
    #share own clothes
    #pbpy.shareown(1-1,28-1)
    
    #share some other people's clothes from feed
    #pbpy.sharecom(50)

    
    