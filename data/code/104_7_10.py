from datetime import datetime, timezone, timedelta

class TimeDeltaCalculator:
    def __init__(self, dt1: datetime, dt2: datetime):
        self.validate_tz(dt1)
        self.validate_tz(dt2)
        self.dt1 = dt1.astimezone(timezone.utc)
        self.dt2 = dt2.astimezone(timezone.utc)

    def validate_tz(self, dt: datetime):
        if dt.tzinfo is None:
            raise ValueError("Datetime must be timezone-aware")

    def get_delta_hours(self) -> float:
        delta = self.dt1 - self.dt2
        return delta.total_seconds() / 3600

    def get_delta_seconds(self) -> float:
        delta = self.dt1 - self.dt2
        return delta.total_seconds()

    def get_delta_timedelta(self) -> timedelta:
        return self.dt1 - self.dt2

if __name__ == '__main__':
    tz = timezone(timedelta(hours=5))
    dt_start = datetime(2023, 1, 1, 10, 0, 0, tzinfo=tz)
    dt_end = datetime(2023, 1, 1, 13, 30, 0, tzinfo=tz)
    calc = TimeDeltaCalculator(dt_start, dt_end)
    print(calc.get_delta_hours())
    print(calc.get_delta_seconds())
    print(calc.get_delta_timedelta())