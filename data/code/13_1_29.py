from datetime import datetime
import pytz

class TimeScaleManager:

    def convert_time(self, from_timezone, to_timezone, time_str):
        try:
            naive_time = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
            from_tz = pytz.timezone(from_timezone)
            aware_time = from_tz.localize(naive_time)
            to_tz = pytz.timezone(to_timezone)
            converted_time = aware_time.astimezone(to_tz)
            return converted_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')
        except Exception as e:
            return str(e)
if __name__ == '__main__':
    manager = TimeScaleManager()
    from_tz = 'America/New_York'
    to_tz = 'Europe/London'
    time_str = '2023-10-15 12:00:00'
    converted_time = manager.convert_time(from_tz, to_tz, time_str)
    print(converted_time)