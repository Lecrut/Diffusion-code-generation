import datetime
import pytz

def convert_timezone(dt, target_tz_str):
    try:
        utc_dt = dt.astimezone(pytz.utc)
        target_tz = pytz.timezone(target_tz_str)
        converted_dt = utc_dt.astimezone(target_tz)
        return converted_dt
    except Exception as e:
        raise ValueError(f'Error converting timezone: {e}')
if __name__ == '__main__':
    sample_dt = datetime.datetime(2023, 10, 5, 14, 30, tzinfo=pytz.utc)
    target_timezone = 'America/New_York'
    converted_datetime = convert_timezone(sample_dt, target_timezone)
    print(converted_datetime)