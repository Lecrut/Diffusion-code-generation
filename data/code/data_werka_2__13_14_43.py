from datetime import datetime
import pytz

def convert_timezones(timestamps, from_tz, to_tz):
    timezone_map = {
        'UTC': pytz.utc,
        'America/New_York': pytz.timezone('America/New_York'),
        'Europe/London': pytz.timezone('Europe/London'),
        'Asia/Tokyo': pytz.timezone('Asia/Tokyo')
    }
    
    if from_tz not in timezone_map or to_tz not in timezone_map:
        raise ValueError(f"Invalid timezone: {from_tz} or {to_tz}")
    
    converted_times = []
    for timestamp in timestamps:
        naive_datetime = datetime.fromisoformat(timestamp)
        localized_datetime = timezone_map[from_tz].localize(naive_datetime)
        converted_datetime = localized_datetime.astimezone(timezone_map[to_tz])
        converted_times.append(converted_datetime.isoformat())
    
    return converted_times

if __name__ == '__main__':
    sample_timestamps = [
        '2023-10-01T12:00:00',
        '2023-10-02T15:30:00',
        '2023-10-03T09:45:00'
    ]
    from_tz = 'America/New_York'
    to_tz = 'Europe/London'
    
    converted_timestamps = convert_timezones(sample_timestamps, from_tz, to_tz)
    for ts in converted_timestamps:
        print(ts)