from datetime import datetime, timedelta

def get_next_month_date(start_date):
    year = start_date.year
    month = start_date.month
    day = start_date.day
    if month == 12:
        next_year = year + 1
        next_month = 1
    else:
        next_year = year
        next_month = month + 1
    try:
        next_date = datetime(next_year, next_month, day)
    except ValueError:
        if month == 2 and day == 29:
            next_date = datetime(next_year, 3, 1)
        else:
            next_date = datetime(next_year, next_month, 1) + timedelta(days=day - 1)
    return next_date
if __name__ == '__main__':
    start_date = datetime(2023, 1, 15)
    next_month_date = get_next_month_date(start_date)
    print(next_month_date.strftime('%Y-%m-%d'))