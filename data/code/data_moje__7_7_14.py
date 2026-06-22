import pytz
from datetime import datetime

def convert_timezone(dt, target_tz_name):
    if dt.tzinfo is None:
        dt = pytz.UTC.localize(dt)
    target_tz = pytz.timezone(target_tz_name)
    return dt.astimezone(target_tz)

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 25, 14, 30, 0)
    result = convert_timezone(sample_dt, 'America/New_York')
    print(result)