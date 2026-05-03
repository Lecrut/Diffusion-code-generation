from datetime import datetime
import pytz
class TimeScaleManager:
    def convert_time(self, dt_str, from_tz_str, to_tz_str):
        dt_object = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
        from_tz = pytz.timezone(from_tz_str)
        to_tz = pytz.timezone(to_tz_str)
        dt_aware = from_tz.localize(dt_object)
        dt_converted = dt_aware.astimezone(to_tz)
        return dt_converted.strftime("%Y-%m-%d %H:%M:%S %Z%z")
if __name__ == '__main__':
    manager = TimeScaleManager()
    time_str = "2023-03-12 01:30:00"
    from_tz = "America/New_York"
    to_tz = "Europe/London"
    converted_time = manager.convert_time(time_str, from_tz, to_tz)
    print(f"Original Time: {time_str} in {from_tz}")
    print(f"Converted Time: {converted_time}")
    time_str_2 = "2023-10-27 10:00:00"
    from_tz_2 = "Asia/Tokyo"
    to_tz_2 = "Asia/Tokyo"
    converted_time_2 = manager.convert_time(time_str_2, from_tz_2, to_tz_2)
    print(f"\nOriginal Time: {time_str_2} in {from_tz_2}")
    print(f"Converted Time: {converted_time_2}")
    time_str_3 = "2023-07-15 12:00:00"
    from_tz_3 = "America/Los_Angeles"
    to_tz_3 = "Australia/Sydney"
    converted_time_3 = manager.convert_time(time_str_3, from_tz_3, to_tz_3)
    print(f"\nOriginal Time: {time_str_3} in {from_tz_3}")
    print(f"Converted Time: {converted_time_3}")