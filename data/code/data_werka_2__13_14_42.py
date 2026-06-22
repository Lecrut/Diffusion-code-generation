from datetime import datetime
import pytz

def validate_timestamp(timestamp):
    try:
        datetime.fromisoformat(timestamp)
    except ValueError:
        raise ValueError(f"Invalid timestamp format: {timestamp}")

def convert_timezones(timestamps, from_tz, to_tz):
    validate_timezone(from_tz)
    validate_timezone(to_tz)
    converted_times = []
    from_timezone = pytz.timezone(from_tz)
    to_timezone = pytz.timezone(to_tz)
    for timestamp in timestamps:
        validate_timestamp(timestamp)
        naive_datetime = datetime.fromisoformat(timestamp)
        localized_datetime = from_timezone.localize(naive_datetime)
        converted_datetime = localized_datetime.astimezone(to_timezone)
        converted_times.append(converted_datetime.isoformat())
    return converted_times

def validate_timezone(timezone_str):
    try:
        pytz.timezone(timezone_str)
    except pytz.UnknownTimeZoneError:
        raise ValueError(f"Invalid timezone: {timezone_str}")

if __name__ == '__main__':
    sample_timestamps = [
        '2023-10-01T12:00:00',
        '2023-10-02T15:30:00',
        '2023-10-03T09:45:00'
    ]
    from_tz = 'America/New_York'
    to_tz = 'Europe/London'
    converted_times = convert_timezones(sample_timestamps, from_tz, to_tz)
    print(converted_times)