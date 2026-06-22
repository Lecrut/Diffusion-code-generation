from datetime import datetime
import pytz

def convert_timezones(timestamps, from_tz, to_tz):
    converted_times = []
    try:
        from_timezone = pytz.timezone(from_tz)
        to_timezone = pytz.timezone(to_tz)
        
        for timestamp in timestamps:
            naive_datetime = datetime.fromisoformat(timestamp)
            localized_datetime = from_timezone.localize(naive_datetime)
            converted_datetime = localized_datetime.astimezone(to_timezone)
            converted_times.append(converted_datetime.isoformat())
    except Exception as e:
        raise ValueError(f"Error converting timezones: {e}")
    
    return converted_times

if __name__ == '__main__':
    timestamps = [
        "2023-10-01T12:00:00",
        "2023-10-02T15:30:00",
        "2023-10-03T09:45:00"
    ]
    from_tz = 'America/New_York'
    to_tz = 'Europe/London'
    
    converted_times = convert_timezones(timestamps, from_tz, to_tz)
    for time in converted_times:
        print(time)