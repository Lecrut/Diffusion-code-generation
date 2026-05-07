import sys
from datetime import datetime
date_str1 = "2023-10-27"
date_str2 = "2023-10-27"
def check_dates(date_str1, date_str2):
    try:
        date1 = datetime.strptime(date_str1, "%Y-%m-%d").date()
        date2 = datetime.strptime(date_str2, "%Y-%m-%d").date()
        return date1 == date2
    except ValueError:
        return False
if __name__ == '__main__':
    result = check_dates(date_str1, date_str2)
    if result:
        print("The dates are the same.")
    else:
        print("The dates are different or invalid.")