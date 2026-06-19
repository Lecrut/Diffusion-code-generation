from datetime import datetime
import pytz

class TimeScaleManager:
    def __init__(self, from_timezone, to_timezone):
        self.from_zone = pytz.timezone(from_timezone)
        self.to_zone = pytz.timezone(to_timezone)

    def convert_time(self, time_str):
        naive_time = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
        localized_time = self.from_zone.localize(naive_time)
        converted_time = localized_time.astimezone(self.to_zone)
        return converted_time.strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    manager = TimeScaleManager('America/New_York', 'Europe/London')
    time_to_convert = '2023-10-15 12:00:00'
    converted_time = manager.convert_time(time_to_convert)
    print(converted_time)