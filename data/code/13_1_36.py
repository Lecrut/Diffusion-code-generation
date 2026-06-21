from datetime import datetime
import pytz

class TimeScaleManager:
    def __init__(self):
        self.time_format = '%Y-%m-%d %H:%M:%S'
    
    def _parse_time(self, time_str):
        return datetime.strptime(time_str, self.time_format)
    
    def _localize_time(self, naive_time, tz_str):
        timezone = pytz.timezone(tz_str)
        return timezone.localize(naive_time)
    
    def _convert_timezone(self, localized_time, to_tz_str):
        to_timezone = pytz.timezone(to_tz_str)
        return localized_time.astimezone(to_timezone)
    
    def convert_time(self, time_str, from_tz, to_tz):
        try:
            naive_time = self._parse_time(time_str)
            localized_time = self._localize_time(naive_time, from_tz)
            converted_time = self._convert_timezone(localized_time, to_tz)
            return converted_time.strftime(f'{self.time_format} %Z%z')
        except Exception as e:
            raise ValueError(f"Error converting time: {e}")

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