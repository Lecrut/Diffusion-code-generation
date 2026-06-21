from datetime import datetime, timedelta

class DateTimeComparator:
    def __init__(self, dt1: datetime, dt2: datetime):
        self.dt1 = dt1.replace(tzinfo=None)
        self.dt2 = dt2.replace(tzinfo=None)

    def get_difference_in_seconds(self) -> int:
        return abs((self.dt1 - self.dt2).total_seconds())

if __name__ == '__main__':
    dt1 = datetime(2023, 4, 1, 12, 0, 0)
    dt2 = datetime(2023, 4, 1, 12, 0, 5)
    comparator = DateTimeComparator(dt1, dt2)
    print(comparator.get_difference_in_seconds())