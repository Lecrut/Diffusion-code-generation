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
        except (pytz.UnknownTimeZoneError, ValueError) as e:
            raise ValueError(f'Invalid timezone or time format: {e}')
if __name__ == '__main__':
    manager = TimeScaleManager()
    try:
        converted_time = manager.convert_time('2023-10-15 14:00:00', 'America/New_York', 'Europe/London')
        print(converted_time)
    except ValueError as e:
        print(e)