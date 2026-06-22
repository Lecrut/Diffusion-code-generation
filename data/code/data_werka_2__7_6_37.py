import pytz
from datetime import datetime

def convert_timezone(dt, target_tz):
    if not isinstance(dt, datetime):
        raise ValueError('Input must be a datetime object')
    try:
        target_timezone = pytz.timezone(target_tz)
    except pytz.UnknownTimeZoneError:
        raise ValueError(f'Unknown timezone: {target_tz}')
    localized_dt = dt.astimezone(pytz.utc).astimezone(target_timezone)
    return localized_dt
if __name__ == '__main__':
    sample_datetime = datetime(2023, 10, 5, 14, 30)
    target_timezone = 'America/New_York'
    converted_time = convert_timezone(sample_datetime, target_timezone)
    print(converted_time)