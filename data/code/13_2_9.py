from datetime import datetime
import pytz
class TimeScaleManager:
    def convert_timezone(self, dt_aware: datetime, target_tz_name: str) -> datetime:
        if dt_aware.tzinfo is None or dt_aware.tzinfo.utcoffset(dt_aware) is None:
            raise ValueError("Input datetime must be timezone-aware")
        target_tz = pytz.timezone(target_tz_name)
        if dt_aware.tzinfo == target_tz:
            return dt_aware
        converted_dt = dt_aware.astimezone(target_tz)
        return converted_dt
if __name__ == '__main__':
    manager = TimeScaleManager()
    dt_est = datetime(2024, 3, 10, 10, 0, 0, tzinfo=pytz.timezone('America/New_York'))
    dt_edt = datetime(2024, 7, 10, 10, 0, 0, tzinfo=pytz.timezone('America/New_York'))
    print(f"Original EDT time: {dt_edt}")
    dt_utc = manager.convert_timezone(dt_edt, 'UTC')
    print(f"Converted to UTC: {dt_utc}")
    dt_gmt = manager.convert_timezone(dt_edt, 'GMT')
    print(f"Converted to GMT: {dt_gmt}")
    dt_ny_spring = datetime(2024, 3, 10, 1, 30, 0, tzinfo=pytz.timezone('America/New_York'))
    print(f"\nTime near DST transition in New York: {dt_ny_spring}")
    dt_ny_spring_utc = manager.convert_timezone(dt_ny_spring, 'UTC')
    print(f"Converted to UTC: {dt_ny_spring_utc}")
    dt_london = manager.convert_timezone(dt_ny_spring, 'Europe/London')
    print(f"Converted to London: {dt_london}")