from datetime import datetime, timedelta, timezone

class DateTimeComparator:
    def __init__(self, dt1: datetime, dt2: datetime):
        if dt1.tzinfo is None or dt2.tzinfo is None:
            raise ValueError("Both datetime objects must be timezone-aware")
        self.dt1_utc = dt1.astimezone(timezone.utc)
        self.dt2_utc = dt2.astimezone(timezone.utc)

    def get_time_difference_in_hours(self) -> float:
        delta = self.dt2_utc - self.dt1_utc
        return abs(delta.total_seconds()) / 3600

if __name__ == '__main__':
    dt1 = datetime(2023, 4, 1, 12, 0, tzinfo=timezone.utc)
    dt2 = datetime(2023, 4, 1, 9, 0, tzinfo=timezone(timedelta(hours=-5)))
    comparator = DateTimeComparator(dt1, dt2)
    print(comparator.get_time_difference_in_hours())