import pytz
from datetime import datetime

def convert_timezone(dt, target_tz_name):
    if dt.tzinfo is None:
        raise ValueError("The provided datetime object must be timezone-aware.")
    source_tz = dt.tzinfo
    target_tz = pytz.timezone(target_tz_name)
    utc_dt = dt.astimezone(pytz.utc)
    converted_dt = utc_dt.astimezone(target_tz)
    return converted_dt

if __name__ == '__main__':
    naive_dt = datetime(2023, 10, 27, 15, 30, 0)
    eastern_tz = pytz.timezone('US/Eastern')
    aware_dt = eastern_tz.localize(naive_dt)
    target_timezone = 'Asia/Tokyo'
    result = convert_timezone(aware_dt, target_timezone)
    print(result)
    print(result.strftime("%Y-%m-%d %H:%M:%S %Z%z"))