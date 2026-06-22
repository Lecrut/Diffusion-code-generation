from datetime import datetime
import pytz

class TimeScaleManager:

    def convert_time(self, time_str, from_tz, to_tz):
        try:
            naive_time = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
            from_timezone = pytz.timezone(from_tz)
            localized_time = from_timezone.localize(naive_time)
            to_timezone = pytz.timezone(to_tz)
            converted_time = localized_time.astimezone(to_timezone)
            return converted_time.strftime('%Y-%m-%d %H:%M:%S')
        except Exception as e:
            raise ValueError(f'Error converting time: {e}')
if __name__ == '__main__':
    time_str = '2023-10-15 14:00:00'
    from_tz = 'America/New_York'
    to_tz = 'Europe/London'
    manager = TimeScaleManager()
    converted_time = manager.convert_time(time_str, from_tz, to_tz)
    print(converted_time)