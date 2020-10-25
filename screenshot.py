# Use pip3 for python3 and pip for older versions
# Install python3-pip using 'sudo apt install python3-pip'
# Install using 'sudo pip3 install pyscreenshot'
import pyscreenshot
import os
import datetime, threading, time

def screenshotFunc(interval):
    imageCount = 0;
    
    while True:
        # Capture screenshot
        image = pyscreenshot.grab()

        # Display captured screenshot
        # image.show();
        
        # Create folder for screenshots
        if not os.path.exists('screenshots'):
            os.makedirs('screenshots')
        
        # Save screenshot
        imageName = 'image%d' % imageCount
        image.save('screenshots/%s.png' % imageName)
        imageCount += 1
        time.sleep(interval)
        

class Main:
            
    def main(self):
    
        interval = 10

        t4 = threading.Thread(target=screenshotFunc, args=[interval], daemon=True)
        t4.start()
        
        time.sleep(21)
        
        return
 
m = Main() 
m.main()
