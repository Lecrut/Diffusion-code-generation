import datetime

class DateComparator:
    def __init__(self, date1: datetime.date, date2: datetime.date):
        self._date1 = date1
        self._date2 = date2

    def __eq__(self) -> bool:
        return self._date1 == self._date2

    def is_greater_than(self) -> bool:
        return self._date1 > self._date2

    def is_less_than(self) -> bool:
        return self._date1 < self._date2

if __name__ == '__main__':
    date_a = datetime.date(2023, 10, 26)
    date_b = datetime.date(2023, 10, 25)
    comparator = DateComparator(date_a, date_b)
    print(f"Date A equals Date B: {comparator.__eq__()}")
    print(f"Date A is greater than Date B: {comparator.is_greater_than()}")
    print(f"Date A is less than Date B: {comparator.is_less_than()}")