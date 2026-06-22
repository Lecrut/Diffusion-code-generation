import datetime
import time

def date_difference(start_date: datetime.date, end_date: datetime.date) -> int:
    delta = end_date - start_date
    return delta.days

def datetime_difference(start_dt: datetime.datetime, end_dt: datetime.datetime) -> float:
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
    print(date_difference(d1, d2))

    dt1 = datetime.datetime(2023, 3, 11, 1, 59, 59)
    dt2 = datetime.datetime(2023, 3, 12, 3, 0, 0)
    print(datetime_difference(dt1, dt2))