from datetime import datetime
import pytz

class TimeScaleManager:

    def convert_time(self, from_time_str, from_tz_str, to_tz_str):
        from_time = datetime.strptime(from_time_str, '%Y-%m-%d %H:%M:%S')
        from_timezone = pytz.timezone(from_tz_str)
        localized_from_time = from_timezone.localize(from_time)
        to_timezone = pytz.timezone(to_tz_str)
        converted_time = localized_from_time.astimezone(to_timezone)
        return converted_time.strftime('%Y-%m-%d %H:%M:%S')
if __name__ == '__main__':
    manager = TimeScaleManager()
    from_time = '2023-10-15 14:00:00'
    from_tz = 'America/New_York'
    to_tz = 'Europe/London'
    converted_time = manager.convert_time(from_time, from_tz, to_tz)
    print(converted_time)