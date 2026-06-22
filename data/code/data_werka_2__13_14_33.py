from datetime import datetime
import pytz

def convert_timezones(timestamps, from_tz, to_tz):
    converted_times = []
    from_timezone = pytz.timezone(from_tz)
    to_timezone = pytz.timezone(to_tz)
    
    for timestamp in timestamps:
        naive_datetime = datetime.fromisoformat(timestamp)
        localized_datetime = from_timezone.localize(naive_datetime)
        converted_datetime = localized_datetime.astimezone(to_timezone)
        converted_times.append(converted_datetime.isoformat())
    
    return converted_times

if __name__ == '__main__':
    sample_timestamps = [
        '2023-10-01T12:00:00',
        '2023-10-02T15:30:00',
        '2023-10-03T09:45:00'
    ]
    from_timezone = 'America/New_York'
    to_timezone = 'Europe/London'
    
    converted_times = convert_timezones(sample_timestamps, from_timezone, to_timezone)
    for time in converted_times:
        print(time)