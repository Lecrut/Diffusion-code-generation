import datetime
import pytz
class TimeNormalizer:
    def normalize(self, dt1: datetime.datetime, dt2: datetime.datetime) -> tuple[datetime.datetime, datetime.datetime]:
        utc1 = dt1.astimezone(pytz.utc)
        utc2 = dt2.astimezone(pytz.utc)
        return utc1, utc2
if __name__ == '__main__':
    import datetime
    import pytz
    tz_ny = pytz.timezone('America/New_York')
    tz_london = pytz.timezone('Europe/London')
    dt_ny_1 = datetime.datetime(2023, 10, 27, 10, 30, 0, tzinfo=tz_ny)
    dt_london_2 = datetime.datetime(2023, 10, 27, 16, 30, 0, tzinfo=tz_london)
    normalizer = TimeNormalizer()
    utc1, utc2 = normalizer.normalize(dt_ny_1, dt_london_2)
    print(f"Original DT1: {dt_ny_1}")
    print(f"Original DT2: {dt_london_2}")
    print(f"Normalized UTC 1: {utc1}")
    print(f"Normalized UTC 2: {utc2}")