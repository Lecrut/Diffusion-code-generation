import datetime
import time

def date_difference(start_date: datetime.date, end_date: datetime.date) -> int:
    delta = end_date - start_date
    return delta.days

def naive_datetime_difference(start_dt: datetime.datetime, end_dt: datetime.datetime) -> datetime.timedelta:
    if start_dt.tzinfo is None or end_dt.tzinfo is None:
        raise ValueError("Both datetimes must be timezone-aware to handle DST correctly.")
    start_utc = start_dt.astimezone(datetime.timezone.utc)
    end_utc = end_dt.astimezone(datetime.timezone.utc)
    return end_utc - start_utc

if __name__ == '__main__':
    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2023, 12, 31)
    days_diff = date_difference(start_date, end_date)
    print(days_diff)

    tz_ny = datetime.timezone(datetime.timedelta(hours=-5))
    tz_london = datetime.timezone(datetime.timedelta(hours=0))
    
    start_naive = datetime.datetime(2023, 3, 11, 1, 0, 0)
    end_naive = datetime.datetime(2023, 3, 12, 1, 0, 0)
    
    start_aware = start_naive.replace(tzinfo=tz_ny)
    end_aware = end_naive.replace(tzinfo=tz_london)
    
    time_diff = naive_datetime_difference(start_aware, end_aware)
    print(time_diff.total_seconds())