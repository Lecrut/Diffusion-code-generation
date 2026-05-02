from datetime import datetime
import pytz
class TimeScaleManager:
    def convert_timezone(self, dt_str, from_tz_str, to_tz_str):
        dt_obj = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
        from_tz = pytz.timezone(from_tz_str)
        to_tz = pytz.timezone(to_tz_str)
        dt_aware = from_tz.localize(dt_obj)
        dt_converted = dt_aware.astimezone(to_tz)
        return dt_converted.strftime("%Y-%m-%d %H:%M:%S %Z%z")
if __name__ == '__main__':
    manager = TimeScaleManager()
    time_str_std = "2024-03-09 10:00:00"
    from_tz_std = "America/New_York"
    to_tz_std = "Europe/London"
    result_std = manager.convert_timezone(time_str_std, from_tz_std, to_tz_std)
    print(f"Original Time: {time_str_std} in {from_tz_std}")
    print(f"Converted Time: {result_std}")
    time_str_dst = "2024-03-11 10:00:00"
    from_tz_dst = "America/New_York"
    to_tz_dst = "Europe/London"
    result_dst = manager.convert_timezone(time_str_dst, from_tz_dst, to_tz_dst)
    print(f"\nOriginal Time: {time_str_dst} in {from_tz_dst}")
    print(f"Converted Time: {result_dst}")
    time_str_transition = "2024-03-10 01:30:00"
    from_tz_transition = "America/New_York"
    to_tz_transition = "Europe/London"
    result_transition = manager.convert_timezone(time_str_transition, from_tz_transition, to_tz_transition)
    print(f"\nOriginal Time (Transition): {time_str_transition} in {from_tz_transition}")
    print(f"Converted Time (Transition): {result_transition}")