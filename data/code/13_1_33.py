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
            return converted_time.strftime('%Y-%m-%d %H:%M:%S')
        except Exception as e:
            raise ValueError(f'Error converting time: {e}')
if __name__ == '__main__':
    manager = TimeScaleManager()
    sample_time = '2023-10-15 14:00:00'
    from_timezone = 'America/New_York'
    to_timezone = 'Europe/London'
    converted_time = manager.convert_time(sample_time, from_timezone, to_timezone)
    print(converted_time)