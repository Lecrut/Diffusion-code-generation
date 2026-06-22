import pytz
from datetime import datetime

def convert_timezone(dt, target_tz_name):
    if dt.tzinfo is None:
        raise ValueError("The input datetime object must be timezone-aware.")
    
    target_tz = pytz.timezone(target_tz_name)
    return dt.astimezone(target_tz)

if __name__ == '__main__':
    utc_tz = pytz.utc
    naive_dt = datetime(2023, 10, 27, 12, 0, 0)
    aware_dt = utc_tz.localize(naive_dt)
    converted_dt = convert_timezone(aware_dt, 'America/New_York')
    print(converted_dt)