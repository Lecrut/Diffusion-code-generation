import calendar
from datetime import datetime

def days_left_in_current_month():
    now = datetime.now()
    year = now.year
    month = now.month
    last_day = calendar.monthrange(year, month)[1]
    current_day = now.day
    return last_day - current_day

if __name__ == '__main__':
    result = days_left_in_current_month()
    print(result)