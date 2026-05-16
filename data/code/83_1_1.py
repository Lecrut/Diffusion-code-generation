import sys
from datetime import datetime
date1_str = "2023-10-27"
date2_str = "2023-10-27"
def check_dates(date_str1, date_str2):
    try:
        date1 = datetime.strptime(date_str1, "%Y-%m-%d")
        date2 = datetime.strptime(date_str2, "%Y-%m-%d")
        if date1 == date2:
            return True
        else:
            return False
    except ValueError:
        return False
if __name__ == '__main__':
    result = check_dates(date1_str, date2_str)
    if result:
        print("The dates are the same.")
    else:
        print("The dates are different or invalid.")