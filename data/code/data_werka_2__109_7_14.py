import datetime
import calendar

def get_seconds_remaining_in_current_month():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    days_in_month = calendar.monthrange(year, month)[1]
    next_month_start = datetime.datetime(year, month + 1 if month < 12 else 1, 1)
    if month == 12:
        next_month_start = datetime.datetime(year + 1, 1, 1)
    else:
        next_month_start = datetime.datetime(year, month + 1, 1)
    delta = next_month_start - now
    return int(delta.total_seconds())

if __name__ == '__main__':
    result = get_seconds_remaining_in_current_month()
    print(result)