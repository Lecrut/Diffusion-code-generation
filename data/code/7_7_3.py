import pytz
from datetime import datetime

def convert_timezone(dt, target_tz_name):
    if dt.tzinfo is None:
        raise ValueError("The provided datetime object must be timezone-aware.")
    utc_dt = dt.astimezone(pytz.utc)
    target_tz = pytz.timezone(target_tz_name)
    return utc_dt.astimezone(target_tz)

if __name__ == '__main__':
    source_tz = pytz.timezone('America/New_York')
    naive_dt = datetime(2023, 11, 5, 14, 30, 0)
    aware_dt = source_tz.localize(naive_dt)
    result = convert_timezone(aware_dt, 'Asia/Tokyo')
    print(result)