from datetime import datetime
import pytz

def validate_timezone(timezone_str):
    try:
        pytz.timezone(timezone_str)
    except pytz.UnknownTimeZoneError:
        raise ValueError(f"Invalid timezone: {timezone_str}")

def convert_timezones(timestamps, from_tz, to_tz):
    validate_timezone(from_tz)
    validate_timezone(to_tz)
    
    converted_times = []
    from_timezone = pytz.timezone(from_tz)
    to_timezone = pytz.timezone(to_tz)
    
    for timestamp in timestamps:
        try:
            naive_datetime = datetime.fromisoformat(timestamp)
            localized_datetime = from_timezone.localize(naive_datetime)
            converted_datetime = localized_datetime.astimezone(to_timezone)
            converted_times.append(converted_datetime.isoformat())
        except (ValueError, TypeError) as e:
            raise ValueError(f"Invalid timestamp {timestamp}: {e}")
    
    return converted_times

if __name__ == '__main__':
    sample_timestamps = [
        '2023-10-01T12:00:00',
        '2023-10-02T15:30:00',
        '2023-10-03T09:45:00'
    ]
    
    from_tz = 'America/New_York'
    to_tz = 'Europe/London'
    
    try:
        converted_timestamps = convert_timezones(sample_timestamps, from_tz, to_tz)
        for original, converted in zip(sample_timestamps, converted_timestamps):
            print(f"Original: {original} -> Converted: {converted}")
    except ValueError as e:
        print(e)