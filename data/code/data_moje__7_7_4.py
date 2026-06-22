import pytz
from datetime import datetime

def convert_timezone(dt, source_tz_name, target_tz_name):
    source_tz = pytz.timezone(source_tz_name)
    target_tz = pytz.timezone(target_tz_name)
    
    if dt.tzinfo is None:
        dt = source_tz.localize(dt)
    else:
        dt = dt.astimezone(source_tz)
    
    converted_dt = dt.astimezone(target_tz)
    return converted_dt

if __name__ == '__main__':
    naive_dt = datetime(2023, 10, 15, 12, 30, 0)
    source_tz = 'US/Eastern'
    target_tz = 'Asia/Tokyo'
    
    result = convert_timezone(naive_dt, source_tz, target_tz)
    print(result)