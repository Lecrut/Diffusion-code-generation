import datetime

class DateComparator:
    def __init__(self, first: datetime.date, second: datetime.date):
        if not isinstance(first, datetime.date) or not isinstance(second, datetime.date):
            raise ValueError("Inputs must be date objects")
        self._first = first
        self._second = second

    @property
    def first(self):
        return self._first

    @property
    def second(self):
        return self._second

    def is_equal(self) -> bool:
        return self._first == self._second

    def is_greater_than(self) -> bool:
        return self._first > self._second

    def is_less_than(self) -> bool:
        return self._first < self._second

    def compare(self) -> int:
        if self._first < self._second:
            return -1
        if self._first > self._second:
            return 1
        return 0

if __name__ == '__main__':
    d1 = datetime.date(2023, 10, 15)
    d2 = datetime.date(2023, 10, 15)
    d3 = datetime.date(2024, 1, 1)
    comp = DateComparator(d1, d3)
    print(comp.is_equal())
    print(comp.is_greater_than())
    print(comp.is_less_than())
    print(comp.compare())