from datetime import datetime
import pytz

class TimeScaleManager:

    def convert_time(self, time_str, from_tz, to_tz):
        naive_time = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
        from_timezone = pytz.timezone(from_tz)
        localized_time = from_timezone.localize(naive_time)
        to_timezone = pytz.timezone(to_tz)
        converted_time = localized_time.astimezone(to_timezone)
        return converted_time.strftime('%Y-%m-%d %H:%M:%S')
if __name__ == '__main__':
    manager = TimeScaleManager()
    sample_time = '2023-10-15 14:00:00'
    from_timezone = 'America/New_York'
    to_timezone = 'Europe/London'
    converted_time = manager.convert_time(sample_time, from_timezone, to_timezone)
    print(converted_time)