import calendar
from datetime import datetime, timedelta

_MONTH_OFFSETS = {
    1: 0, 2: 31, 3: 59, 4: 90, 5: 120, 6: 151,
    7: 181, 8: 212, 9: 243, 10: 273, 11: 304, 12: 334
}

def days_left_in_current_month() -> int:
    now = datetime.now()
    year = now.year
    month = now.month
    _, days_in_month = calendar.monthrange(year, month)
    days_passed = now.day
    return days_in_month - days_passed

if __name__ == '__main__':
    result = days_left_in_current_month()
    print(result)