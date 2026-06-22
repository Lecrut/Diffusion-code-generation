import datetime
import pytz

def convert_timezone(dt, target_tz_name):
    if dt.tzinfo is not None:
        dt_utc = dt.astimezone(pytz.utc)
    else:
        dt_utc = pytz.utc.localize(dt)
    target_tz = pytz.timezone(target_tz_name)
    converted_dt = dt_utc.astimezone(target_tz)
    return converted_dt

if __name__ == '__main__':
    source_dt = datetime.datetime(2023, 10, 25, 12, 0, 0)
    target_tz = 'US/Eastern'
    result = convert_timezone(source_dt, target_tz)
    print(result)