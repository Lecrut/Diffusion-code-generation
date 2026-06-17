import sys
from datetime import datetime
def compare_dates(date_str1, date_str2):
    try:
        date1 = datetime.strptime(date_str1, '%Y-%m-%d')
        date2 = datetime.strptime(date_str2, '%Y-%m-%d')
        if date1 < date2:
            print("Date 1 is before Date 2")
        elif date1 == date2:
            print("Date 1 is the same as Date 2")
        else:
            print("Date 1 is after Date 2")
    except ValueError:
        print("Error: Invalid date format. Please use YYYY-MM-DD.")
if __name__ == '__main__':
    date1_input = "2023-01-15"
    date2_input = "2023-02-20"
    compare_dates(date1_input, date2_input)