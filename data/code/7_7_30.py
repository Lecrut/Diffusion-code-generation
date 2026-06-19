import datetime
import pytz

def convert_timezone(dt, target_tz_str):
    source_tz = pytz.utc
    dt_utc = source_tz.localize(dt)
    target_tz = pytz.timezone(target_tz_str)
    return dt_utc.astimezone(target_tz)
if __name__ == '__main__':
    sample_dt = datetime.datetime(2023, 10, 15, 14, 30)
    target_timezone = 'America/New_York'
    converted_time = convert_timezone(sample_dt, target_timezone)
    print(converted_time)