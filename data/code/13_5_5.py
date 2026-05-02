import datetime
import pytz
class TimeNormalizer:
    def normalize_to_utc(self, dt1: datetime.datetime, dt2: datetime.datetime) -> tuple[datetime.datetime, datetime.datetime]:
        if dt1.tzinfo is None or dt2.tzinfo is None:
            raise ValueError("Both input datetimes must be timezone-aware.")
        dt1_utc = dt1.astimezone(pytz.utc)
        dt2_utc = dt2.astimezone(pytz.utc)
        return dt1_utc, dt2_utc
if __name__ == '__main__':
    tz_ny = pytz.timezone('America/New_York')
    tz_london = pytz.timezone('Europe/London')
    dt_ny_time = datetime.datetime(2023, 10, 27, 14, 30, 0, tzinfo=tz_ny)
    dt_london_time = datetime.datetime(2023, 10, 27, 19, 30, 0, tzinfo=tz_london)
    normalizer = TimeNormalizer()
    try:
        dt1_utc, dt2_utc = normalizer.normalize_to_utc(dt_ny_time, dt_london_time)
        print(f"Original NY Time: {dt_ny_time}")
        print(f"Original London Time: {dt_london_time}")
        print("-" * 30)
        print(f"Normalized UTC Time 1: {dt1_utc}")
        print(f"Normalized UTC Time 2: {dt2_utc}")
    except ValueError as e:
        print(f"Error: {e}")