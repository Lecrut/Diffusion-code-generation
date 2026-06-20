import pytz
from datetime import datetime

def convert_timezone(dt, target_tz_name):
    if dt.tzinfo is None:
        dt = pytz.utc.localize(dt)
    target_tz = pytz.timezone(target_tz_name)
    converted_dt = dt.astimezone(target_tz)
    return converted_dt

if __name__ == '__main__':
    source_dt = datetime(2023, 10, 1, 12, 0, 0)
    target_tz_name = "US/Pacific"
    result = convert_timezone(source_dt, target_tz_name)
    print(result)