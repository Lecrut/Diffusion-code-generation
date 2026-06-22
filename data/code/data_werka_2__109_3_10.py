import calendar
from datetime import datetime, timedelta

_MONTH_NAMES = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}

def get_days_left_in_current_month() -> int:
    now = datetime.now()
    year = now.year
    month = now.month
    last_day_of_month = calendar.monthrange(year, month)[1]
    days_passed = now.day
    days_left = last_day_of_month - days_passed
    return days_left

if __name__ == '__main__':
    result = get_days_left_in_current_month()
    print(result)