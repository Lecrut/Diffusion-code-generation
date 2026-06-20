import datetime
import pytz

def is_timezone_aware(dt):
    return dt.tzinfo is not None and dt.utcoffset() is not None

def normalize_to_utc(dt, tz):
    if dt.tzinfo != tz:
        dt = dt.astimezone(tz)
    return dt

def calculate_time_difference(dt1, dt2):
    if not (is_timezone_aware(dt1) and is_timezone_aware(dt2)):
        raise ValueError("Both datetime objects must be timezone-aware.")
    
    utc_dt1 = normalize_to_utc(dt1, pytz.utc)
    utc_dt2 = normalize_to_utc(dt2, pytz.utc)
    
    return utc_dt2 - utc_dt1

if __name__ == '__main__':
    tz_london = pytz.timezone('Europe/London')
    tz_new_york = pytz.timezone('America/New_York')
    
    dt_london_time = datetime.datetime(2023, 10, 26, 10, 0, 0, tzinfo=tz_london)
    dt_new_york_time = datetime.datetime(2023, 10, 26, 5, 0, 0, tzinfo=tz_new_york)
    
    try:
        time_diff = calculate_time_difference(dt_london_time, dt_new_york_time)
        print(f"Time Difference: {time_diff}")
    except ValueError as e:
        print(e)