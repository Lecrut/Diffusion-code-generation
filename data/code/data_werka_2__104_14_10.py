import datetime

class DateComparator:
    def __init__(self, date1: datetime.date, date2: datetime.date):
        self._date1 = date1
        self._date2 = date2

    @property
    def date1(self):
        return self._date1

    @property
    def date2(self):
        return self._date2

    def is_equal(self) -> bool:
        return self._date1 == self._date2

    def is_greater_than(self) -> bool:
        return self._date1 > self._date2

    def is_less_than(self) -> bool:
        return self._date1 < self._date2

if __name__ == '__main__':
    d1 = datetime.date(2023, 10, 1)
    d2 = datetime.date(2023, 10, 1)
    d3 = datetime.date(2023, 10, 2)

    comp1 = DateComparator(d1, d2)
    comp2 = DateComparator(d1, d3)

    print(comp1.is_equal())
    print(comp2.is_less_than())
    print(comp2.is_greater_than())