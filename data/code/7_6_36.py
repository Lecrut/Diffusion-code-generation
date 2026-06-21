import pytz
from datetime import datetime

def convert_timezone(dt, target_tz):
    if not isinstance(dt, datetime):
        raise ValueError('Input must be a datetime object')
    try:
        target_timezone = pytz.timezone(target_tz)
    except pytz.UnknownTimeZoneError:
        raise ValueError(f'Unknown timezone: {target_tz}')
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=pytz.utc)
    else:
        dt = dt.astimezone(pytz.utc)
    return dt.astimezone(target_timezone)
if __name__ == '__main__':
    SAMPLE_DATETIME = datetime(2023, 10, 15, 14, 30)
    TARGET_TIMEZONE = 'Europe/London'
    CONVERTED_TIME = convert_timezone(SAMPLE_DATETIME, TARGET_TIMEZONE)
    print(CONVERTED_TIME)