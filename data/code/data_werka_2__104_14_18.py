import datetime

_DAYS_IN_WEEK = 7
_MONTHS_IN_YEAR = 12
_COMPARISON_RESULT_EQUAL = 0
_COMPARISON_RESULT_GREATER = 1
_COMPARISON_RESULT_LESS = -1

class DateComparator:
    def __init__(self, date1, date2):
        if not isinstance(date1, datetime.date):
            raise ValueError("date1 must be a date instance")
        if not isinstance(date2, datetime.date):
            raise ValueError("date2 must be a date instance")
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

    def compare_to(self):
        if self._date1 == self._date2:
            return _COMPARISON_RESULT_EQUAL
        if self._date1 > self._date2:
            return _COMPARISON_RESULT_GREATER
        return _COMPARISON_RESULT_LESS

    def days_difference(self):
        delta = self._date1 - self._date2
        return delta.days

    def is_weeks_apart(self):
        diff_days = self.days_difference()
        return diff_days % _DAYS_IN_WEEK == 0

    def year_diff(self):
        return abs(self._date1.year - self._date2.year)

    def month_diff(self):
        return abs((self._date1.year - self._date2.year) * _MONTHS_IN_YEAR + (self._date1.month - self._date2.month))

if __name__ == '__main__':
    d1 = datetime.date(2023, 10, 15)
    d2 = datetime.date(2023, 10, 10)
    comparator = DateComparator(d1, d2)
    print(comparator.is_greater_than())
    print(comparator.days_difference())
    print(comparator.year_diff())