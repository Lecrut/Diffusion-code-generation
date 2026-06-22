import datetime

SECONDS_PER_DAY = 86400
MINUTES_PER_HOUR = 60

def compute_date_delta_days(start: datetime.date, end: datetime.date) -> int:
    delta = end - start
    return delta.days

def compute_timedelta_seconds_utc(start_dt: datetime.datetime, end_dt: datetime.datetime) -> float:
    if start_dt.tzinfo is None or end_dt.tzinfo is None:
        raise ValueError("Both datetimes must be timezone-aware to handle DST correctly.")
    start_utc = start_dt.astimezone(datetime.timezone.utc)
    end_utc = end_dt.astimezone(datetime.timezone.utc)
    return (end_utc - start_utc).total_seconds()

def get_timestamp_now_utc() -> int:
    return int(datetime.datetime.now(datetime.timezone.utc).timestamp())

if __name__ == '__main__':
    start_date_obj = datetime.date(2024, 1, 1)
    end_date_obj = datetime.date(2024, 12, 31)
    days_result = compute_date_delta_days(start_date_obj, end_date_obj)
    print(days_result)
    
    tz_est = datetime.timezone(datetime.timedelta(hours=-5))
    dt_start = datetime.datetime(2024, 1, 1, 12, 0, 0, tzinfo=tz_est)
    dt_end = datetime.datetime(2024, 1, 2, 12, 0, 0, tzinfo=tz_est)
    seconds_result = compute_timedelta_seconds_utc(dt_start, dt_end)
    print(seconds_result)
    
    current_ts = get_timestamp_now_utc()
    print(current_ts)