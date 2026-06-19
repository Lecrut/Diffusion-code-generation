import pytz
from datetime import datetime

class TimeScaleManager:

    def __init__(self, from_tz_str, to_tz_str):
        self.from_tz = pytz.timezone(from_tz_str)
        self.to_tz = pytz.timezone(to_tz_str)

    def convert_time(self, naive_datetime_str):
        naive_datetime = datetime.strptime(naive_datetime_str, '%Y-%m-%d %H:%M:%S')
        localized_from = self.from_tz.localize(naive_datetime)
        converted_to = localized_from.astimezone(self.to_tz)
        return converted_to.strftime('%Y-%m-%d %H:%M:%S')
if __name__ == '__main__':
    manager = TimeScaleManager('America/New_York', 'Europe/London')
    result = manager.convert_time('2023-10-25 14:00:00')
    print(result)