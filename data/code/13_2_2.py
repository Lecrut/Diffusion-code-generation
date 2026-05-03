import datetime
import pytz
class TimeScaleManager:
    def convert_time(self, dt_str, from_tz_str, to_tz_str):
        dt_obj = datetime.datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
        from_tz = pytz.timezone(from_tz_str)
        to_tz = pytz.timezone(to_tz_str)
        dt_aware = from_tz.localize(dt_obj)
        dt_converted = dt_aware.astimezone(to_tz)
        return dt_converted.strftime("%Y-%m-%d %H:%M:%S %Z%z")
if __name__ == '__main__':
    manager = TimeScaleManager()
    time_str_1 = "2023-03-12 10:00:00"
    from_tz_1 = "America/New_York"
    to_tz_1 = "Europe/London"
    result_1 = manager.convert_time(time_str_1, from_tz_1, to_tz_1)
    print(f"Original Time: {time_str_1} ({from_tz_1})")
    print(f"Converted Time: {result_1}")
    print("-" * 20)
    time_str_2a = "2023-03-12 01:30:00"
    from_tz_2a = "America/New_York"
    to_tz_2a = "Europe/London"
    result_2a = manager.convert_time(time_str_2a, from_tz_2a, to_tz_2a)
    print(f"Time before DST change: {time_str_2a} ({from_tz_2a})")
    print(f"Converted Time (Before): {result_2a}")
    print("-" * 20)
    time_str_2b = "2023-03-12 03:30:00"
    from_tz_2b = "America/New_York"
    to_tz_2b = "Europe/London"
    result_2b = manager.convert_time(time_str_2b, from_tz_2b, to_tz_2b)
    print(f"Time after DST change: {time_str_2b} ({from_tz_2b})")
    print(f"Converted Time (After): {result_2b}")
    print("-" * 20)