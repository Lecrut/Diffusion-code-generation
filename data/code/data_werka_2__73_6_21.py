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
    elif start_dt.tzinfo is None and end_dt.tzinfo is None:
        start_dt = start_dt.replace(tzinfo=datetime.timezone.utc)
        end_dt = end_dt.replace(tzinfo=datetime.timezone.utc)
    
    delta = end_dt - start_dt
    total_seconds = delta.total_seconds()
    return total_seconds / 3600.0

if __name__ == '__main__':
    start_d = datetime.date(2023, 1, 1)
    end_d = datetime.date(2023, 12, 31)
    days_diff = date_difference(start_d, end_d)
    print(days_diff)
    
    start_dt = datetime.datetime(2023, 3, 10, 1, 0, 0)
    end_dt = datetime.datetime(2023, 3, 10, 13, 0, 0)
    hours_diff = datetime_difference(start_dt, end_dt)
    print(hours_diff)