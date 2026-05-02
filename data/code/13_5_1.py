import datetime
import pytz
class TimeNormalizer:
    def normalize_to_utc(self, dt1: datetime.datetime, dt2: datetime.datetime) -> tuple[datetime.datetime, datetime.datetime]:
        if dt1.tzinfo is None or dt2.tzinfo is None:
            raise ValueError("Both datetime objects must be timezone-aware.")
        dt1_utc = dt1.astimezone(pytz.utc)
        dt2_utc = dt2.astimezone(pytz.utc)
        return dt1_utc, dt2_utc
if __name__ == '__main__':
    import datetime
    import pytz
    tz_ny = pytz.timezone('America/New_York')
    tz_london = pytz.timezone('Europe/London')
    dt_ny_1 = datetime.datetime(2023, 10, 27, 10, 30, 0, tzinfo=tz_ny)
    dt_london_2 = datetime.datetime(2023, 10, 27, 15, 30, 0, tzinfo=tz_london)
    normalizer = TimeNormalizer()
    try:
        dt1_utc, dt2_utc = normalizer.normalize_to_utc(dt_ny_1, dt_london_2)
        print(f"Original dt1 (NY): {dt_ny_1}")
        print(f"Original dt2 (London): {dt_london_2}")
        print("-" * 30)
        print(f"Normalized dt1 (UTC): {dt1_utc}")
        print(f"Normalized dt2 (UTC): {dt2_utc}")
    except ValueError as e:
        print(f"Error: {e}")