class DateComparator:
    def __init__(self, date1, date2):
        self._date1 = date1
        self._date2 = date2

    @property
    def date1(self):
        return self._date1

    @property
    def date2(self):
        return self._date2

    def is_equal(self):
        return self._date1 == self._date2

    def is_greater_than(self):
        return self._date1 > self._date2

    def is_less_than(self):
        return self._date1 < self._date2

if __name__ == '__main__':
    from datetime import date

    d1 = date(2023, 10, 1)
    d2 = date(2023, 10, 2)

    comparator = DateComparator(d1, d2)

    print(comparator.is_equal())
    print(comparator.is_greater_than())
    print(comparator.is_less_than())