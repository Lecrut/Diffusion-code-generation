import pytz
from datetime import datetime

def convert_timezone(dt, target_tz_name):
    if dt.tzinfo is None:
        local_tz = pytz.timezone('UTC')
        dt = local_tz.localize(dt)
    else:
        dt = dt.astimezone(pytz.UTC)
    target_tz = pytz.timezone(target_tz_name)
    converted_dt = dt.astimezone(target_tz)
    return converted_dt

if __name__ == '__main__':
    dt = datetime(2023, 10, 15, 12, 0, 0)
    result = convert_timezone(dt, 'America/New_York')
    print(result)