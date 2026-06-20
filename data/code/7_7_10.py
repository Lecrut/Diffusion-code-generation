import datetime
import pytz

def convert_timezone(dt: datetime.datetime, target_tz_name: str) -> datetime.datetime:
    if dt.tzinfo is None:
        utc_dt = pytz.utc.localize(dt)
    else:
        utc_dt = dt.astimezone(pytz.utc)
    target_tz = pytz.timezone(target_tz_name)
    converted_dt = utc_dt.astimezone(target_tz)
    return converted_dt

if __name__ == '__main__':
    naive_dt = datetime.datetime(2023, 10, 15, 12, 0, 0)
    target_zone = 'America/New_York'
    result = convert_timezone(naive_dt, target_zone)
    print(result)