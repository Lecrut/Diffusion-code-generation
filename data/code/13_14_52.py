from datetime import datetime
import pytz

def convert_timestamps(timestamps, from_tz_str, to_tz_str):
    from_tz = pytz.timezone(from_tz_str)
    to_tz = pytz.timezone(to_tz_str)
    
    converted_times = []
    for ts in timestamps:
        naive_dt = datetime.fromisoformat(ts)
        aware_dt = from_tz.localize(naive_dt)
        converted_dt = aware_dt.astimezone(to_tz)
        converted_times.append(converted_dt.isoformat())
    
    return converted_times

if __name__ == '__main__':
    sample_timestamps = [
        '2023-10-01T12:00:00',
        '2023-10-02T15:30:00',
        '2023-10-03T09:45:00'
    ]
    from_timezone = 'America/New_York'
    to_timezone = 'Europe/London'
    
    converted_times = convert_timestamps(sample_timestamps, from_timezone, to_timezone)
    for time in converted_times:
        print(time)