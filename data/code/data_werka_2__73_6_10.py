import datetime
import time

def date_difference_days(start_date: datetime.date, end_date: datetime.date) -> int:
    delta = end_date - start_date
    return delta.days

def date_difference_seconds(start_dt: datetime.datetime, end_dt: datetime.datetime) -> float:
    if start_dt.tzinfo is None or end_dt.tzinfo is None:
        naive_start = start_dt.replace(tzinfo=datetime.timezone.utc) if start_dt.tzinfo is None else start_dt
        naive_end = end_dt.replace(tzinfo=datetime.timezone.utc) if end_dt.tzinfo is None else end_dt
        delta = naive_end - naive_start
    else:
        delta = end_dt - start_dt
    return delta.total_seconds()

if __name__ == '__main__':
    d1 = datetime.date(2023, 1, 1)
    d2 = datetime.date(2023, 12, 31)
    print(date_difference_days(d1, d2))

    dt1 = datetime.datetime(2023, 3, 11, 1, 0, 0)
    dt2 = datetime.datetime(2023, 3, 12, 1, 0, 0)
    print(date_difference_seconds(dt1, dt2))

    tz = datetime.timezone(datetime.timedelta(hours=-5))
    dt3 = datetime.datetime(2023, 11, 4, 1, 0, 0, tzinfo=tz)
    dt4 = datetime.datetime(2023, 11, 5, 1, 0, 0, tzinfo=tz)
    print(date_difference_seconds(dt3, dt4))