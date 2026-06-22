import datetime

class DateComparator:
    def __init__(self, date1: datetime.date, date2: datetime.date):
        self._date1 = date1
        self._date2 = date2

    def is_equal(self) -> bool:
        return self._date1 == self._date2

    def is_greater_than(self) -> bool:
        return self._date1 > self._date2

    def is_less_than(self) -> bool:
        return self._date1 < self._date2

    def __eq__(self, other):
        if not isinstance(other, DateComparator):
            return NotImplemented
        return self._date1 == other._date1 and self._date2 == other._date2

    def __hash__(self):
        return hash((self._date1, self._date2))

if __name__ == '__main__':
    d1 = datetime.date(2023, 10, 1)
    d2 = datetime.date(2023, 10, 2)
    d3 = datetime.date(2023, 10, 1)

    comp = DateComparator(d1, d2)
    print(comp.is_less_than())
    print(comp.is_greater_than())
    print(comp.is_equal())

    comp2 = DateComparator(d1, d3)
    print(comp2.is_equal())
    print(comp == comp2)