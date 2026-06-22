import calendar
from datetime import datetime

def days_left_in_current_month():
    today = datetime.now()
    year = today.year
    month = today.month
    last_day = calendar.monthrange(year, month)[1]
    days_elapsed = today.day
    return last_day - days_elapsed

if __name__ == '__main__':
    result = days_left_in_current_month()
    print(result)