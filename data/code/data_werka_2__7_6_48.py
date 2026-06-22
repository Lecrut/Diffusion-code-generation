import pytz
from datetime import datetime

def convert_timezone(dt, target_tz):
    if not isinstance(dt, datetime):
        raise ValueError('Input must be a datetime object')
    try:
        source_tz = dt.tzinfo
        if source_tz is None:
            raise ValueError('Datetime object must have timezone information')
        target_timezone = pytz.timezone(target_tz)
        localized_dt = source_tz.localize(dt) if not dt.tzinfo else dt
        converted_dt = localized_dt.astimezone(target_timezone)
        return converted_dt
    except pytz.UnknownTimeZoneError:
        raise ValueError(f'Unknown timezone: {target_tz}')
if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 5, 14, 30, tzinfo=pytz.timezone('UTC'))
    target_timezone = 'America/New_York'
    converted_datetime = convert_timezone(sample_dt, target_timezone)
    print(converted_datetime)