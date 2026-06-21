import pytz
from datetime import datetime

def convert_timezone(dt, target_tz):
    if not isinstance(dt, datetime):
        raise ValueError('Input must be a datetime object')
    try:
        target_timezone = pytz.timezone(target_tz)
    except pytz.UnknownTimeZoneError:
        raise ValueError(f'Unknown timezone: {target_tz}')
    local_dt = dt.replace(tzinfo=pytz.utc) if dt.tzinfo is None else dt.astimezone(pytz.utc)
    return local_dt.astimezone(target_timezone)
if __name__ == '__main__':
    sample_datetime = datetime(2023, 10, 5, 14, 30)
    target_timezone = 'America/New_York'
    converted_time = convert_timezone(sample_datetime, target_timezone)
    print(converted_time)