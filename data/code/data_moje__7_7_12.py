import datetime
import pytz

def convert_timezone(dt, source_tz_str, target_tz_str):
    source_tz = pytz.timezone(source_tz_str)
    target_tz = pytz.timezone(target_tz_str)
    if dt.tzinfo is None:
        dt = source_tz.localize(dt)
    converted_dt = dt.astimezone(target_tz)
    return converted_dt

if __name__ == '__main__':
    sample_dt = datetime.datetime(2023, 10, 15, 14, 30, 0)
    result = convert_timezone(sample_dt, 'US/Eastern', 'Europe/London')
    print(result)