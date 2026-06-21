from datetime import datetime
import pytz

def convert_timezone(dt, target_tz):
    if not isinstance(dt, datetime):
        raise ValueError('Input must be a datetime object')
    if not isinstance(target_tz, str) or target_tz not in pytz.all_timezones:
        raise ValueError('Invalid timezone specified')
    try:
        source_tz = dt.tzinfo
        if source_tz is None:
            source_tz = pytz.utc
            dt = dt.replace(tzinfo=source_tz)
        target_timezone = pytz.timezone(target_tz)
        return dt.astimezone(target_timezone)
    except Exception as e:
        raise ValueError(f'Error converting timezone: {e}')
if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 5, 14, 30, tzinfo=None)
    target_timezone = 'America/New_York'
    converted_time = convert_timezone(sample_dt, target_timezone)
    print(converted_time)