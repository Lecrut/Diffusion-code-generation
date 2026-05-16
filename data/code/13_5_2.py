from datetime import datetime, timezone, timedelta
class TimeNormalizer:
    def normalize_to_utc(self, dt1: datetime, dt2: datetime) -> tuple[datetime, datetime]:
        utc1 = dt1.astimezone(timezone.utc)
        utc2 = dt2.astimezone(timezone.utc)
        return utc1, utc2
if __name__ == '__main__':
    import pytz
    tz_london = pytz.timezone('Europe/London')
    tz_tokyo = pytz.timezone('Asia/Tokyo')
    dt_london_time = datetime(2023, 10, 27, 14, 30, 0, tzinfo=tz_london)
    dt_tokyo_time = datetime(2023, 10, 27, 23, 30, 0, tzinfo=tz_tokyo)
    normalizer = TimeNormalizer()
    utc1, utc2 = normalizer.normalize_to_utc(dt_london_time, dt_tokyo_time)
    print(f"Original London Time: {dt_london_time}")
    print(f"Original Tokyo Time: {dt_tokyo_time}")
    print(f"Normalized UTC 1: {utc1}")
    print(f"Normalized UTC 2: {utc2}")