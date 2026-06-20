from datetime import datetime, timedelta

def next_month(start_date):
    year = start_date.year
    month = start_date.month
    day = start_date.day
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    try:
        return datetime(year, month, day)
    except ValueError:
        last_day_of_new_month = datetime(year, month, 1) + timedelta(days=32)
        return datetime(year, month, last_day_of_new_month.day - 1)
if __name__ == '__main__':
    start_date = datetime(2023, 11, 30)
    print(next_month(start_date))