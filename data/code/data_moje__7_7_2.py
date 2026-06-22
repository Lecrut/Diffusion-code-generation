import pytz
from datetime import datetime

def convert_timezone(dt, target_tz_name):
    if dt is None:
        raise ValueError("datetime object cannot be None")
    if target_tz_name is None:
        raise ValueError("Time zone name cannot be None")
    
    if dt.tzinfo is not None:
        dt_utc = dt.astimezone(pytz.utc)
    else:
        dt_utc = pytz.utc.localize(dt)
    
    target_tz = pytz.timezone(target_tz_name)
    converted_dt = dt_utc.astimezone(target_tz)
    return converted_dt

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 25, 12, 0, 0)
    sample_tz = "America/New_York"
    result = convert_timezone(sample_dt, sample_tz)
    print(result)