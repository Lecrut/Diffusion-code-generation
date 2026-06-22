import pytz
from datetime import datetime

def convert_timezone(dt: datetime, target_tz_name: str) -> datetime:
    if dt.tzinfo is None:
        raise ValueError("The input datetime must have timezone information.")
    
    local_tz = dt.tzinfo
    utc_dt = dt.astimezone(pytz.utc)
    
    target_tz = pytz.timezone(target_tz_name)
    target_dt = utc_dt.astimezone(target_tz)
    
    return target_dt

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 27, 15, 30, 0, tzinfo=pytz.timezone('America/New_York'))
    target_zone = 'Asia/Tokyo'
    result = convert_timezone(sample_dt, target_zone)
    print(result)