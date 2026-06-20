import pytz
from datetime import datetime

def convert_timezone(dt, target_tz_str):
    if dt.tzinfo is None:
        dt = pytz.utc.localize(dt)
    target_tz = pytz.timezone(target_tz_str)
    return dt.astimezone(target_tz)

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 15, 12, 0, 0)
    converted = convert_timezone(sample_dt, 'America/New_York')
    print(converted)