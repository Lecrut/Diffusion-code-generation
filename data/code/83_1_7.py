import datetime

class DateTimeComparator:
    def __init__(self, dt1: datetime.datetime, dt2: datetime.datetime):
        self.dt1 = dt1
        self.dt2 = dt2

    def compare_ignoring_time(self) -> bool:
        return self.dt1.date() == self.dt2.date()

if __name__ == '__main__':
    comparator = DateTimeComparator(
        datetime.datetime(2023, 4, 15, 12, 30),
        datetime.datetime(2023, 4, 15, 18, 45)
    )
    result = comparator.compare_ignoring_time()
    print(result)