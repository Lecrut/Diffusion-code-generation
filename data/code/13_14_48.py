from datetime import datetime
import pytz

def convert_timestamps(timestamps, from_tz, to_tz):
    converted_times = []
    for timestamp in timestamps:
        naive_time = datetime.fromisoformat(timestamp)
        localized_time = from_tz.localize(naive_time)
        converted_time = localized_time.astimezone(to_tz)
        converted_times.append(converted_time.isoformat())
    return converted_times

if __name__ == '__main__':
    sample_timestamps = [
        '2023-10-01T12:00:00',
        '2023-10-02T15:30:00'
    ]
    from_timezone = pytz.timezone('America/New_York')
    to_timezone = pytz.timezone('Europe/London')
    
    converted_times = convert_timestamps(sample_timestamps, from_timezone, to_timezone)
    print(converted_times)