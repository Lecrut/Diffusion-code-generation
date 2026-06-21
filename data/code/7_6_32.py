import pytz
from datetime import datetime

def convert_timezone(dt, target_tz):
    try:
        if dt.tzinfo is None:
            raise ValueError('Input datetime must be timezone-aware')
        utc_dt = dt.astimezone(pytz.utc)
        target_timezone = pytz.timezone(target_tz)
        converted_dt = utc_dt.astimezone(target_timezone)
        return converted_dt
    except pytz.UnknownTimeZoneError:
        raise ValueError('Unknown timezone')
if __name__ == '__main__':
    sample_datetime = datetime(2023, 10, 5, 14, 30, tzinfo=pytz.utc)
    target_timezone = 'Asia/Shanghai'
    converted_datetime = convert_timezone(sample_datetime, target_timezone)
    print(converted_datetime)