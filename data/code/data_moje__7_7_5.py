import pytz
from datetime import datetime

def convert_timezone(dt, target_tz_name):
    utc_tz = pytz.utc
    target_tz = pytz.timezone(target_tz_name)
    if dt.tzinfo is None:
        dt = utc_tz.localize(dt)
    else:
        dt = dt.astimezone(utc_tz)
    return dt.astimezone(target_tz)

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 25, 12, 0, 0)
    result = convert_timezone(sample_dt, 'America/New_York')
    print(result)