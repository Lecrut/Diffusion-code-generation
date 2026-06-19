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
    sample_dt = datetime(2023, 10, 5, 14, 30, tzinfo=pytz.utc)
    target_tz = 'America/New_York'
    converted_datetime = convert_timezone(sample_dt, target_tz)
    print(converted_datetime)