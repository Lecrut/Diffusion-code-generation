import pytz
from datetime import datetime

def convert_timezone(dt, target_tz_name):
    if dt is None:
        raise ValueError("Datetime object cannot be None")
    if target_tz_name is None:
        raise ValueError("Target time zone name cannot be None")
    target_tz = pytz.timezone(target_tz_name)
    if dt.tzinfo is None:
        dt = pytz.utc.localize(dt)
    converted_dt = dt.astimezone(target_tz)
    return converted_dt

if __name__ == '__main__':
    source_dt = datetime(2023, 10, 15, 12, 0, 0)
    result = convert_timezone(source_dt, 'America/New_York')
    print(result)