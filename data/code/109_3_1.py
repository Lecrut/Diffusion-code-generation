import calendar
from datetime import datetime

_MONTH_DAYS = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

def days_left_in_current_month():
    now = datetime.now()
    year = now.year
    month = now.month
    days_in_month = _MONTH_DAYS[month]
    if month == 2 and calendar.isleap(year):
        days_in_month = 29
    days_passed = now.day
    days_left = days_in_month - days_passed
    return days_left

if __name__ == '__main__':
    result = days_left_in_current_month()
    print(result)