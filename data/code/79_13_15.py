from datetime import datetime, timedelta

def get_next_month_date(start_date):
    year = start_date.year
    month = start_date.month + 1
    day = start_date.day
    if month > 12:
        year += 1
        month = 1
    try:
        next_month_date = datetime(year, month, day)
    except ValueError:
        if month == 2 and day == 29:
            next_month_date = datetime(year, month, 28)
        else:
            next_month_date = datetime(year, month, 1)
    return next_month_date
if __name__ == '__main__':
    start_date = datetime(2023, 1, 15)
    next_month_date = get_next_month_date(start_date)
    print(next_month_date.strftime('%Y-%m-%d'))