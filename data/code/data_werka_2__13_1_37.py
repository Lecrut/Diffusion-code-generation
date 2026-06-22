from datetime import datetime
import pytz

class TimeScaleManager:
    TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

    def __init__(self):
        self.supported_timezones = set(pytz.all_timezones)

    def convert_time(self, time_str, from_tz, to_tz):
        if from_tz not in self.supported_timezones or to_tz not in self.supported_timezones:
            raise ValueError("One or both of the provided timezones are not supported.")
        
        try:
            naive_time = datetime.strptime(time_str, self.TIME_FORMAT)
            from_timezone = pytz.timezone(from_tz)
            localized_time = from_timezone.localize(naive_time)
            to_timezone = pytz.timezone(to_tz)
            converted_time = localized_time.astimezone(to_timezone)
            return converted_time.strftime(self.TIME_FORMAT + ' %Z%z')
        except Exception as e:
            raise ValueError(f'Error converting time: {e}')

if __name__ == '__main__':
    manager = TimeScaleManager()
    sample_time = '2023-10-15 14:00:00'
    from_timezone = 'America/New_York'
    to_timezone = 'Europe/London'
    try:
        converted_time = manager.convert_time(sample_time, from_timezone, to_timezone)
        print(converted_time)
    except ValueError as e:
        print(e)