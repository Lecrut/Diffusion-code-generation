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
    date_time_str_1 = "2023-03-15 10:00:00"
    from_tz_1 = "America/New_York"
    to_tz_1 = "Europe/London"
    result_1 = manager.convert_timezone(date_time_str_1, from_tz_1, to_tz_1)
    print(f"Original: {date_time_str_1} in {from_tz_1}")
    print(f"Converted: {result_1} in {to_tz_1}")
    print("-" * 20)
    date_time_str_2 = "2023-03-12 01:30:00"
    from_tz_2 = "America/New_York"
    to_tz_2 = "Europe/Paris"
    result_2 = manager.convert_timezone(date_time_str_2, from_tz_2, to_tz_2)
    print(f"Original: {date_time_str_2} in {from_tz_2}")
    print(f"Converted: {result_2} in {to_tz_2}")
    print("-" * 20)
    date_time_str_3 = "2023-11-05 01:30:00"
    from_tz_3 = "America/New_York"
    to_tz_3 = "Europe/Paris"
    result_3 = manager.convert_timezone(date_time_str_3, from_tz_3, to_tz_3)
    print(f"Original: {date_time_str_3} in {from_tz_3}")
    print(f"Converted: {result_3} in {to_tz_3}")