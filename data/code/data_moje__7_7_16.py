import pytz
from datetime import datetime

def convert_to_timezone(dt, source_timezone_str, target_timezone_str):
    source_tz = pytz.timezone(source_timezone_str)
    target_tz = pytz.timezone(target_timezone_str)
    if dt.tzinfo is None:
        localized_dt = source_tz.localize(dt)
    else:
        localized_dt = dt.astimezone(source_tz)
    converted_dt = localized_dt.astimezone(target_tz)
    return converted_dt

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 15, 14, 30, 0)
    result = convert_to_timezone(sample_dt, 'US/Eastern', 'Europe/London')
    print(result)