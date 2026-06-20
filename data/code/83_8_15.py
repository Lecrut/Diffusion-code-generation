import datetime

class DateComparer:
    def __init__(self, date1: datetime.datetime, date2: datetime.datetime):
        self.date1 = date1.date()
        self.date2 = date2.date()

    def compare(self) -> bool:
        return self.date1 == self.date2

if __name__ == '__main__':
    d1 = datetime.datetime(2023, 10, 26, 14, 30)
    d2 = datetime.datetime(2023, 10, 26, 9, 0)
    comparer = DateComparer(d1, d2)
    print(f"Are {d1} and {d2} on the same day? {comparer.compare()}")

    d3 = datetime.datetime(2023, 11, 1, 12, 0)
    comparer = DateComparer(d1, d3)
    print(f"Are {d1} and {d3} on the same day? {comparer.compare()}")