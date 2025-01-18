# Simple program in organizing screenshots

import os
import shutil

screenshot_dir = r"C:\Users\user\Pictures\Screenshots"

MONTHS = ["01-JANUARY", "02-FEBRUARY", "03-MARCH", "04-APRIL", "05-MAY", "06-JUNE", "07-JULY", "08-AUGUST", "09-SEPTEMBER", "10-OCTOBER", "11-NOVEMBER", "12-DECEMBER"]

def check_month(month):
    if month == "01":
        return MONTHS[0]
    elif month == "02":
        return MONTHS[1]
    elif month == "03":
        return MONTHS[2]
    elif month == "04":
        return MONTHS[3]
    elif month == "05":
        return MONTHS[4]
    elif month == "06":
        return MONTHS[5]
    elif month == "07":
        return MONTHS[6]
    elif month == "08":
        return MONTHS[7]
    elif month == "09":
        return MONTHS[8]
    elif month == "10":
        return MONTHS[9]
    elif month == "11":
        return MONTHS[10]
    else:
        return MONTHS[11]

for screenshot in os.listdir(screenshot_dir):
    try:
        date = screenshot.split(" ")[1]
        month = check_month(date.split("-")[1])
        if not os.path.exists(f"C:/Users/user/Pictures/Screenshots/{month}/{date}"):
            os.makedirs(f"C:/Users/user/Pictures/Screenshots/{month}/{date}")
        
        shutil.move(f"C:/Users/user/Pictures/Screenshots/{screenshot}", f"C:/Users/user/Pictures/Screenshots/{month}/{date}")
    except:
        pass



    