from datetime import datetime, timedelta

class DateTimeComparator:
    def __init__(self, dt1: datetime, dt2: datetime):
        if not isinstance(dt1, datetime) or not isinstance(dt2, datetime):
            raise ValueError("Both inputs must be instances of datetime.")
        self.dt1 = dt1
        self.dt2 = dt2

    def get_time_difference_seconds(self) -> int:
        return abs((self.dt1 - self.dt2).total_seconds())

if __name__ == '__main__':
    dt1 = datetime(2023, 10, 1, 12, 0, 0)
    dt2 = datetime(2023, 10, 1, 12, 0, 30)
    comparator = DateTimeComparator(dt1, dt2)
    print(comparator.get_time_difference_seconds())