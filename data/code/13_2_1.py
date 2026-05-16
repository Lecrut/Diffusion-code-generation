from datetime import datetime
import pytz
class TimeScaleManager:
    def convert_time(self, dt_str, source_tz_name, target_tz_name):
        source_tz = pytz.timezone(source_tz_name)
        target_tz = pytz.timezone(target_tz_name)
        dt_naive = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
        dt_aware = source_tz.localize(dt_naive)
        dt_converted = dt_aware.astimezone(target_tz)
        return dt_converted.strftime("%Y-%m-%d %H:%M:%S %Z%z")
if __name__ == '__main__':
    manager = TimeScaleManager()
    date_str = "2023-10-27 10:00:00"
    source_tz = "America/New_York"
    target_tz = "Europe/London"
    result1 = manager.convert_time(date_str, source_tz, target_tz)
    print(f"Original Time: {date_str} in {source_tz}")
    print(f"Converted Time: {result1} in {target_tz}")
    date_str_dst = "2023-11-05 01:30:00"
    source_tz_dst = "America/New_York"
    target_tz_dst = "UTC"
    result2 = manager.convert_time(date_str_dst, source_tz_dst, target_tz_dst)
    print(f"\nOriginal Time (DST test): {date_str_dst} in {source_tz_dst}")
    print(f"Converted Time (DST test): {result2} in {target_tz_dst}")
    date_str_large = "2024-01-15 12:00:00"
    source_tz_large = "Asia/Tokyo"
    target_tz_large = "America/Los_Angeles"
    result3 = manager.convert_time(date_str_large, source_tz_large, target_tz_large)
    print(f"\nOriginal Time: {date_str_large} in {source_tz_large}")
    print(f"Converted Time: {result3} in {target_tz_large}")