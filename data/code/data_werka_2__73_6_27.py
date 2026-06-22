import datetime
import zoneinfo

class DateDeltaCalculator:
    def __init__(self, start: datetime.datetime, end: datetime.datetime):
        self.start = start
        self.end = end

    def _ensure_utc(self, dt: datetime.datetime) -> datetime.datetime:
        if dt.tzinfo is None:
            return dt.replace(tzinfo=datetime.timezone.utc)
        return dt.astimezone(datetime.timezone.utc)

    def get_timedelta(self) -> datetime.timedelta:
        start_utc = self._ensure_utc(self.start)
        end_utc = self._ensure_utc(self.end)
        return end_utc - start_utc

    def get_days(self) -> int:
        return self.get_timedelta().days

    def get_seconds(self) -> float:
        return self.get_timedelta().total_seconds()

if __name__ == '__main__':
    tz_ny = zoneinfo.ZoneInfo("America/New_York")
    tz_london = zoneinfo.ZoneInfo("Europe/London")

    start_dt = datetime.datetime(2023, 3, 11, 1, 0, 0, tzinfo=tz_ny)
    end_dt = datetime.datetime(2023, 3, 12, 1, 0, 0, tzinfo=tz_ny)

    calculator = DateDeltaCalculator(start_dt, end_dt)
    delta = calculator.get_timedelta()
    days = calculator.get_days()
    seconds = calculator.get_seconds()

    print(delta)
    print(days)
    print(seconds)

    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2023, 12, 31)
    date_calc = DateDeltaCalculator(
        start_date.replace(tzinfo=datetime.timezone.utc),
        end_date.replace(tzinfo=datetime.timezone.utc)
    )
    print(date_calc.get_days())