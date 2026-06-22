import datetime

_DATE_COMPARISON_RESULT_NEGATIVE = -1
_DATE_COMPARISON_RESULT_ZERO = 0
_DATE_COMPARISON_RESULT_POSITIVE = 1

class DateComparator:
    def __init__(self, first_date, second_date):
        if not isinstance(first_date, datetime.date):
            raise ValueError("first_date must be a datetime.date object")
        if not isinstance(second_date, datetime.date):
            raise ValueError("second_date must be a datetime.date object")
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
            return _DATE_COMPARISON_RESULT_NEGATIVE
        if self._first > self._second:
            return _DATE_COMPARISON_RESULT_POSITIVE
        return _DATE_COMPARISON_RESULT_ZERO

if __name__ == '__main__':
    d1 = datetime.date(2023, 10, 1)
    d2 = datetime.date(2023, 10, 2)
    comparator = DateComparator(d1, d2)
    print(comparator.is_less_than())
    print(comparator.compare())