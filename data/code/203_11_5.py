from datetime import datetime, timedelta

class DateTimeComparator:
    def __init__(self, dt1: datetime, dt2: datetime):
        self.dt1 = dt1
        self.dt2 = dt2

    def get_time_difference_seconds(self) -> int:
        if self.dt1.tzinfo is None and self.dt2.tzinfo is None:
            return abs((self.dt1 - self.dt2).total_seconds())
        elif self.dt1.tzinfo is not None and self.dt2.tzinfo is not None:
            dt1_utc = self.dt1.astimezone()
            dt2_utc = self.dt2.astimezone()
            return abs((dt1_utc - dt2_utc).total_seconds())
        else:
            raise ValueError("Both datetimes must be timezone-aware or both must be naive.")

if __name__ == '__main__':
    dt1 = datetime(2023, 10, 1, 12, 0, 0, tzinfo=None)
    dt2 = datetime(2023, 10, 1, 12, 0, 5, tzinfo=None)
    comparator = DateTimeComparator(dt1, dt2)
    print(comparator.get_time_difference_seconds())