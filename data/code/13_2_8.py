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
    dt_str_standard = "2024-03-09 23:59:59"
    from_tz_str = "US/Eastern"
    to_tz_str = "US/Eastern"
    result_standard = manager.convert_timezone(dt_str_standard, from_tz_str, to_tz_str)
    print(f"Original: {dt_str_standard} in {from_tz_str} -> Converted: {result_standard}")
    dt_str_dst = "2024-03-10 00:00:00"
    result_dst = manager.convert_timezone(dt_str_dst, from_tz_str, to_tz_str)
    print(f"Original: {dt_str_dst} in {from_tz_str} -> Converted: {result_dst}")
    dt_str_utc = "2024-03-10 00:00:00"
    from_tz_str_utc = "UTC"
    to_tz_str_pacific = "US/Pacific"
    result_cross = manager.convert_timezone(dt_str_utc, from_tz_str_utc, to_tz_str_pacific)
    print(f"Original: {dt_str_utc} in {from_tz_str_utc} -> Converted: {result_cross}")