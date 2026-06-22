from datetime import datetime
import pytz

class TimeScaleManager:

    def __init__(self, from_tz_str, to_tz_str):
        self.from_tz = pytz.timezone(from_tz_str)
        self.to_tz = pytz.timezone(to_tz_str)

    def convert_time(self, time_str):
        naive_time = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
        localized_time = self.from_tz.localize(naive_time)
        converted_time = localized_time.astimezone(self.to_tz)
        return converted_time.strftime('%Y-%m-%d %H:%M:%S')
if __name__ == '__main__':
    manager = TimeScaleManager('America/New_York', 'Europe/London')
    sample_time = '2023-10-15 14:00:00'
    converted_time = manager.convert_time(sample_time)
    print(converted_time)