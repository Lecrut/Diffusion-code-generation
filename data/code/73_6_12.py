import datetime
import sys

class DateCalculator:
    def __init__(self, start: datetime.datetime, end: datetime.datetime):
        self.start = start
        self.end = end

    def get_days_difference(self) -> int:
        if self.start.tzinfo is not None or self.end.tzinfo is not None:
            start_utc = self.start.astimezone(datetime.timezone.utc)
            end_utc = self.end.astimezone(datetime.timezone.utc)
            delta = end_utc - start_utc
        else:
            delta = self.end - self.start
        return delta.days

    def get_seconds_difference(self) -> float:
        if self.start.tzinfo is not None or self.end.tzinfo is not None:
            start_utc = self.start.astimezone(datetime.timezone.utc)
            end_utc = self.end.astimezone(datetime.timezone.utc)
            delta = end_utc - start_utc
        else:
            delta = self.end - self.start
        return delta.total_seconds()

if __name__ == '__main__':
    start_dt = datetime.datetime(2023, 3, 12, 1, 0, 0)
    end_dt = datetime.datetime(2023, 3, 12, 2, 0, 0)
    tz_ny = datetime.timezone(datetime.timedelta(hours=-5))
    tz_london = datetime.timezone(datetime.timedelta(hours=0))
    
    start_aware = start_dt.replace(tzinfo=tz_ny)
    end_aware = end_dt.replace(tzinfo=tz_london)
    
    calc = DateCalculator(start_aware, end_aware)
    print(calc.get_days_difference())
    print(calc.get_seconds_difference())