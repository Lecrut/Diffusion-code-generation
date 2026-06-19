from datetime import datetime
import pytz

class TimeScaleManager:

    def convert_time(self, from_time_str, from_tz, to_tz):
        from_timezone = pytz.timezone(from_tz)
        to_timezone = pytz.timezone(to_tz)
        from_time = datetime.strptime(from_time_str, '%Y-%m-%d %H:%M:%S')
        from_time = from_timezone.localize(from_time)
        to_time = from_time.astimezone(to_timezone)
        return to_time.strftime('%Y-%m-%d %H:%M:%S')
if __name__ == '__main__':
    manager = TimeScaleManager()
    converted_time = manager.convert_time('2023-10-15 12:00:00', 'America/New_York', 'Europe/London')
    print(converted_time)