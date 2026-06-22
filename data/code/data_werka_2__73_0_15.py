import datetime
import pytz

class TimeDeltaCalculator:
    def __init__(self, tz_local: str = 'UTC'):
        self.tz_local = pytz.timezone(tz_local)

    def _normalize_to_utc(self, dt: datetime.datetime) -> datetime.datetime:
        if dt.tzinfo is None:
            raise ValueError("Input datetime must be timezone-aware.")
        return dt.astimezone(pytz.utc)

    def calculate(self, dt_start: datetime.datetime, dt_end: datetime.datetime) -> datetime.timedelta:
        utc_start = self._normalize_to_utc(dt_start)
        utc_end = self._normalize_to_utc(dt_end)
        return utc_end - utc_start

if __name__ == '__main__':
    calc = TimeDeltaCalculator('UTC')
    tz_tokyo = pytz.timezone('Asia/Tokyo')
    tz_paris = pytz.timezone('Europe/Paris')
    dt_tokyo = datetime.datetime(2023, 12, 25, 9, 0, 0, tzinfo=tz_tokyo)
    dt_paris = datetime.datetime(2023, 12, 25, 0, 0, 0, tzinfo=tz_paris)
    delta = calc.calculate(dt_tokyo, dt_paris)
    print(delta)