import pytz
from datetime import datetime

def convert_timezone(dt, target_zone):
    source_zone = dt.tzinfo
    if source_zone is None:
        raise ValueError("The input datetime object must be timezone-aware.")
    local_dt = dt.replace(tzinfo=source_zone)
    target_tz = pytz.timezone(target_zone)
    return local_dt.astimezone(target_tz)

if __name__ == '__main__':
    naive_dt = datetime(2023, 10, 15, 12, 30, 0)
    utc_tz = pytz.UTC
    aware_dt = utc_tz.localize(naive_dt)
    result = convert_timezone(aware_dt, 'America/New_York')
    print(result)