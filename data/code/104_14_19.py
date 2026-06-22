import datetime

class DateComparator:
    def __init__(self, first_date, second_date):
        if not isinstance(first_date, datetime.date):
            raise ValueError("first_date must be a date object")
        if not isinstance(second_date, datetime.date):
            raise ValueError("second_date must be a date object")
        self._first = first_date
        self._second = second_date

    @property
    def first(self):
        return self._first

    @property
    def second(self):
        return self._second

    def is_equal(self):
        return self._first == self._second

    def is_greater_than(self):
        return self._first > self._second

    def is_less_than(self):
        return self._first < self._second

    def compare(self):
        if self._first < self._second:
            return -1
        if self._first > self._second:
            return 1
        return 0

if __name__ == '__main__':
    d1 = datetime.date(2023, 10, 15)
    d2 = datetime.date(2023, 10, 15)
    d3 = datetime.date(2024, 1, 1)
    d4 = datetime.date(2022, 12, 31)

    comp1 = DateComparator(d1, d2)
    comp2 = DateComparator(d3, d4)

    print(comp1.is_equal())
    print(comp2.is_greater_than())
    print(comp1.compare())
    print(comp2.is_less_than())