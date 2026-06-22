import calendar
from datetime import datetime

def days_left_in_current_month():
    now = datetime.now()
    year = now.year
    month = now.month
    _, days_in_month = calendar.monthrange(year, month)
    days_passed = now.day
    return days_in_month - days_passed

if __name__ == '__main__':
    result = days_left_in_current_month()
    print(result)