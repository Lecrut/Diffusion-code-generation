from datetime import datetime, timezone, timedelta
import pytz
class TimeNormalizer:
    def normalize_to_utc(self, dt1: datetime, dt2: datetime) -> tuple[datetime, datetime]:
        if dt1.tzinfo is None or dt2.tzinfo is None:
            raise ValueError("Both input datetimes must be timezone-aware.")
        dt1_utc = dt1.astimezone(timezone.utc)
        dt2_utc = dt2.astimezone(timezone.utc)
        return dt1_utc, dt2_utc
if __name__ == '__main__':
    tz_ny = pytz.timezone('America/New_York')
    dt_ny_1 = datetime(2023, 10, 27, 10, 0, 0, tzinfo=tz_ny)
    dt_ny_2 = datetime(2023, 10, 27, 14, 30, 0, tzinfo=tz_ny)
    dt_utc_1 = datetime(2023, 10, 27, 12, 0, 0, tzinfo=timezone.utc)
    dt_london = datetime(2023, 10, 27, 13, 0, 0, tzinfo=pytz.timezone('Europe/London'))
    normalizer = TimeNormalizer()
    try:
        utc1, utc2 = normalizer.normalize_to_utc(dt_ny_1, dt_ny_2)
        print(f"Original dt1 (NY): {dt_ny_1}")
        print(f"Original dt2 (NY): {dt_ny_2}")
        print("-" * 30)
        print(f"Normalized dt1 (UTC): {utc1}")
        print(f"Normalized dt2 (UTC): {utc2}")
        print("-" * 30)
        print(f"Original dt_utc_1 (UTC): {dt_utc_1}")
        print(f"Original dt_london (London): {dt_london}")
        utc3, utc4 = normalizer.normalize_to_utc(dt_utc_1, dt_london)
        print(f"Normalized dt_utc_1 (UTC): {utc3}")
        print(f"Normalized dt_london (UTC): {utc4}")
    except ValueError as e:
        print(f"Error: {e}")