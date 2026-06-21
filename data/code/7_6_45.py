import pytz
from datetime import datetime

def convert_timezone(dt, target_tz):
    if not isinstance(dt, datetime):
        raise ValueError('Input must be a datetime object')
    if not isinstance(target_tz, str):
        raise ValueError('Target time zone must be a string')
    try:
        source_tz = dt.tzinfo
        if source_tz is None:
            raise ValueError('Source datetime must have timezone information')
        target_timezone = pytz.timezone(target_tz)
        localized_dt = source_tz.localize(dt) if not dt.tzinfo else dt
        converted_dt = localized_dt.astimezone(target_timezone)
        return converted_dt
    except pytz.UnknownTimeZoneError:
        raise ValueError('Unknown time zone')
if __name__ == '__main__':
    sample_datetime = datetime(2023, 10, 5, 14, 30)
    target_timezone = 'America/New_York'
    try:
        converted_time = convert_timezone(sample_datetime, target_timezone)
        print('Converted Time:', converted_time)
    except ValueError as e:
        print(e)