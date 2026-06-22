import pytz
from datetime import datetime

def convert_timezone(dt, target_tz):
    if dt.tzinfo is None:
        raise ValueError('Input datetime must be timezone-aware')
    if dt.tzinfo != pytz.utc:
        dt = pytz.utc.localize(dt)
    target_timezone = pytz.timezone(target_tz)
    converted_dt = dt.astimezone(target_timezone)
    return converted_dt
if __name__ == '__main__':
    sample_datetime = datetime(2023, 10, 5, 14, 30, tzinfo=pytz.utc)
    target_timezone_str = 'America/New_York'
    converted_time = convert_timezone(sample_datetime, target_timezone_str)
    print(converted_time)