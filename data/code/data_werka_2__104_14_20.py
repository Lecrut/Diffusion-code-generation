import datetime

class DateComparator:
    __slots__ = ('_d1', '_d2')

    def __init__(self, d1: datetime.date, d2: datetime.date):
        self._d1 = d1
        self._d2 = d2

    @property
    def date1(self):
        return self._d1

    @property
    def date2(self):
        return self._d2

    def is_equal(self) -> bool:
        return self._d1 == self._d2

    def is_greater_than(self) -> bool:
        return self._d1 > self._d2

    def is_less_than(self) -> bool:
        return self._d1 < self._d2

    def compare(self) -> int:
        if self._d1 < self._d2:
            return -1
        if self._d1 > self._d2:
            return 1
        return 0

if __name__ == '__main__':
    d1 = datetime.date(2023, 10, 1)
    d2 = datetime.date(2023, 10, 1)
    d3 = datetime.date(2023, 10, 2)

    comp1 = DateComparator(d1, d2)
    print(comp1.is_equal())

    comp2 = DateComparator(d1, d3)
    print(comp2.is_less_than())

    comp3 = DateComparator(d3, d1)
    print(comp3.is_greater_than())

    print(comp1.compare())
    print(comp2.compare())
    print(comp3.compare())