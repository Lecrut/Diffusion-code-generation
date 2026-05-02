from datetime import datetime
import pytz
class TimeScaleManager:
    def convert_timezone(self, dt_str, from_tz_str, to_tz_str):
        dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
        from_tz = pytz.timezone(from_tz_str)
        to_tz = pytz.timezone(to_tz_str)
        dt_aware = from_tz.localize(dt)
        dt_converted = dt_aware.astimezone(to_tz)
        return dt_converted.strftime("%Y-%m-%d %H:%M:%S %Z%z")
if __name__ == '__main__':
    manager = TimeScaleManager()
    time_str = "2023-03-12 02:30:00"
    from_tz = "America/New_York"
    to_tz = "Europe/London"
    print(f"Original Time: {time_str} in {from_tz}")
    converted_time = manager.convert_timezone(time_str, from_tz, to_tz)
    print(f"Converted Time: {converted_time}")
    time_str_2 = "2023-10-27 10:00:00"
    from_tz_2 = "America/New_York"
    to_tz_2 = "Asia/Tokyo"
    print(f"\nOriginal Time: {time_str_2} in {from_tz_2}")
    converted_time_2 = manager.convert_timezone(time_str_2, from_tz_2, to_tz_2)
    print(f"Converted Time: {converted_time_2}")