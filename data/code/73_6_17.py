import datetime
import time

def date_difference(start_date: datetime.date, end_date: datetime.date) -> int:
    delta = end_date - start_date
    return delta.days

def datetime_difference(start_dt: datetime.datetime, end_dt: datetime.datetime) -> float:
    if start_dt.tzinfo is None and end_dt.tzinfo is not None:
        start_dt = start_dt.replace(tzinfo=datetime.timezone.utc)
    elif start_dt.tzinfo is not None and end_dt.tzinfo is None:
        end_dt = end_dt.replace(tzinfo=datetime.timezone.utc)
    
    delta = end_dt - start_dt
    total_seconds = delta.total_seconds()
    return total_seconds / 3600.0

if __name__ == '__main__':
    d1 = datetime.date(2023, 1, 1)
    d2 = datetime.date(2023, 12, 31)
    print(date_difference(d1, d2))
    
    dt1 = datetime.datetime(2023, 1, 1, 12, 0, 0)
    dt2 = datetime.datetime(2023, 1, 1, 14, 30, 0)
    print(datetime_difference(dt1, dt2))