import pytz
from datetime import datetime

def convert_timezone(dt, target_tz):
    if not isinstance(dt, datetime):
        raise ValueError("Input must be a datetime object")
    
    try:
        target_timezone = pytz.timezone(target_tz)
    except pytz.UnknownTimeZoneError:
        raise ValueError(f"Unknown timezone: {target_tz}")
    
    if dt.tzinfo is None:
        raise ValueError("Source datetime must have timezone information")
    
    localized_dt = dt.astimezone(pytz.utc) if not dt.tzinfo else dt
    converted_dt = localized_dt.astimezone(target_timezone)
    return converted_dt

if __name__ == '__main__':
    sample_datetime = datetime(2023, 10, 5, 14, 30, tzinfo=pytz.utc)
    target_timezone = 'America/New_York'
    converted_time = convert_timezone(sample_datetime, target_timezone)
    print(converted_time)