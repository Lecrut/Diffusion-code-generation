from datetime import datetime, timedelta

class DateTimeComparator:
    def __init__(self, dt1: datetime, dt2: datetime):
        self.dt1 = dt1
        self.dt2 = dt2

    def get_time_difference_seconds(self) -> int:
        if self.dt1.tzinfo and self.dt2.tzinfo:
            difference = abs((self.dt1 - self.dt2).total_seconds())
        else:
            raise ValueError("Both datetimes must be timezone-aware")
        return int(difference)

if __name__ == '__main__':
    dt1 = datetime(2023, 10, 1, 12, 0, 0, tzinfo=timezone.utc)
    dt2 = datetime(2023, 10, 1, 14, 30, 0, tzinfo=timezone.utc)
    comparator = DateTimeComparator(dt1, dt2)
    print(comparator.get_time_difference_seconds())