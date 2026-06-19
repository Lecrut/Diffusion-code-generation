import pytz
from datetime import datetime

class TimeScaleManager:
    def __init__(self, source_tz, target_tz):
        self.source_tz = pytz.timezone(source_tz)
        self.target_tz = pytz.timezone(target_tz)

    def convert_time(self, time_str):
        naive_datetime = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
        localized_datetime = self.source_tz.localize(naive_datetime)
        converted_datetime = localized_datetime.astimezone(self.target_tz)
        return converted_datetime.strftime("%Y-%m-%d %H:%M:%S")

if __name__ == '__main__':
    time_manager = TimeScaleManager('America/New_York', 'Europe/London')
    sample_time = "2023-10-15 14:00:00"
    converted_time = time_manager.convert_time(sample_time)
    print(converted_time)