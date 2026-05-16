from datetime import datetime, timezone, timedelta
class TimeNormalizer:
    def normalize_to_utc(self, dt1: datetime, dt2: datetime) -> tuple[datetime, datetime]:
        utc1 = dt1.astimezone(timezone.utc)
        utc2 = dt2.astimezone(timezone.utc)
        return utc1, utc2
if __name__ == '__main__':
    import pytz
    tz_ny = pytz.timezone('America/New_York')
    tz_london = pytz.timezone('Europe/London')
    dt_ny_1 = datetime(2023, 10, 27, 10, 30, 0, tzinfo=tz_ny)
    dt_london_2 = datetime(2023, 10, 27, 14, 30, 0, tzinfo=tz_london)
    normalizer = TimeNormalizer()
    utc1, utc2 = normalizer.normalize_to_utc(dt_ny_1, dt_london_2)
    print(f"Original DT1: {dt_ny_1}")
    print(f"Original DT2: {dt_london_2}")
    print(f"Normalized UTC 1: {utc1}")
    print(f"Normalized UTC 2: {utc2}")