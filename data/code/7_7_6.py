import pytz
from datetime import datetime

def convert_timezone(dt, target_tz_name):
    if dt.tzinfo is None:
        raise ValueError("DateTime must be timezone-aware")
    target_tz = pytz.timezone(target_tz_name)
    converted_dt = dt.astimezone(target_tz)
    return converted_dt

if __name__ == '__main__':
    utc = pytz.UTC
    sample_dt = utc.localize(datetime(2023, 10, 1, 12, 0, 0))
    result = convert_timezone(sample_dt, "America/New_York")
    print(result)