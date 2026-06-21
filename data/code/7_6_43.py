from datetime import datetime
import pytz

def convert_timezone(dt, target_tz):
    if not isinstance(dt, datetime):
        raise ValueError("Input must be a datetime object")
    try:
        source_tz = dt.tzinfo or pytz.utc
        localized_dt = source_tz.localize(dt) if source_tz == pytz.utc else dt
        target_timezone = pytz.timezone(target_tz)
        converted_dt = localized_dt.astimezone(target_timezone)
        return converted_dt
    except pytz.UnknownTimeZoneError:
        raise ValueError("Unknown timezone")

if __name__ == '__main__':
    sample_datetime = datetime(2023, 10, 5, 14, 30)
    target_timezone = 'America/New_York'
    converted_time = convert_timezone(sample_datetime, target_timezone)
    print(converted_time)