from datetime import datetime
import pytz

class TimeScaleManager:

    def convert_time(self, time_str, from_tz_str, to_tz_str):
        try:
            naive_time = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
            from_tz = pytz.timezone(from_tz_str)
            localized_time = from_tz.localize(naive_time)
            to_tz = pytz.timezone(to_tz_str)
            converted_time = localized_time.astimezone(to_tz)
            return converted_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')
        except Exception as e:
            return str(e)
if __name__ == '__main__':
    time_str = '2023-10-15 14:00:00'
    from_tz_str = 'America/New_York'
    to_tz_str = 'Europe/London'
    manager = TimeScaleManager()
    converted_time = manager.convert_time(time_str, from_tz_str, to_tz_str)
    print(converted_time)