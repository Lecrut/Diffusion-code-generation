import datetime
import time

def date_difference_days(start_date: datetime.date, end_date: datetime.date) -> int:
    delta = end_date - start_date
    return delta.days

def date_difference_seconds(start_dt: datetime.datetime, end_dt: datetime.datetime) -> float:
    if start_dt.tzinfo is None and end_dt.tzinfo is None:
        delta = end_dt - start_dt
        return delta.total_seconds()
    else:
        delta = end_dt - start_dt
        return delta.total_seconds()

def get_days_between_dates(start_year: int, start_month: int, start_day: int, end_year: int, end_month: int, end_day: int) -> int:
    start_date = datetime.date(start_year, start_month, start_day)
    end_date = datetime.date(end_year, end_month, end_day)
    return date_difference_days(start_date, end_date)
if __name__ == '__main__':
    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2023, 12, 31)
    days_diff = get_days_between_dates(2023, 1, 1, 2023, 12, 31)
    print(days_diff)
    start_dt = datetime.datetime(2023, 3, 10, 12, 0, 0)
    end_dt = datetime.datetime(2023, 3, 11, 12, 0, 0)
    seconds_diff = date_difference_seconds(start_dt, end_dt)
    print(seconds_diff)