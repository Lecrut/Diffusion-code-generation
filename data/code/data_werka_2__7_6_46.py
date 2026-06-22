import pytz
from datetime import datetime

class TimezoneConverter:
    def __init__(self):
        self.utc_zone = pytz.utc

    def convert(self, dt, target_tz):
        if not isinstance(dt, datetime):
            raise ValueError("Input must be a datetime object")
        
        try:
            target_timezone = pytz.timezone(target_tz)
        except pytz.UnknownTimeZoneError:
            raise ValueError(f"Unknown timezone: {target_tz}")
        
        if dt.tzinfo is None:
            local_dt = self.utc_zone.localize(dt)
        else:
            local_dt = dt.astimezone(self.utc_zone)
        
        return local_dt.astimezone(target_timezone)

if __name__ == '__main__':
    converter = TimezoneConverter()
    sample_datetime1 = datetime(2023, 10, 15, 14, 30, tzinfo=pytz.timezone('UTC'))
    target_timezone1 = 'Asia/Shanghai'
    converted_time1 = converter.convert(sample_datetime1, target_timezone1)
    print(converted_time1)

    sample_datetime2 = datetime(2023, 10, 5, 9, 0)
    target_timezone2 = 'America/New_York'
    converted_time2 = converter.convert(sample_datetime2, target_timezone2)
    print(converted_time2)