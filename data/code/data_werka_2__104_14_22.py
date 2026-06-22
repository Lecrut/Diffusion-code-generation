import datetime

_COMPARISON_RESULT_EQUAL = 0
_COMPARISON_RESULT_GREATER = 1
_COMPARISON_RESULT_LESS = -1
_DATE_FORMAT_STR = "%Y-%m-%d"

class DateComparator:
    def __init__(self, first_date: datetime.date, second_date: datetime.date) -> None:
        self._first = first_date
        self._second = second_date

    @property
    def first_date(self) -> datetime.date:
        return self._first

    @property
    def second_date(self) -> datetime.date:
        return self._second

    def is_equal(self) -> bool:
        return self._first == self._second

    def is_greater_than(self) -> bool:
        return self._first > self._second

    def is_less_than(self) -> bool:
        return self._first < self._second

    def get_comparison_result(self) -> int:
        if self._first == self._second:
            return _COMPARISON_RESULT_EQUAL
        if self._first > self._second:
            return _COMPARISON_RESULT_GREATER
        return _COMPARISON_RESULT_LESS

    def format_dates(self) -> str:
        f_str = self._first.strftime(_DATE_FORMAT_STR)
        s_str = self._second.strftime(_DATE_FORMAT_STR)
        return f"{f_str} vs {s_str}"

if __name__ == '__main__':
    date_a = datetime.date(2023, 10, 15)
    date_b = datetime.date(2023, 10, 15)
    date_c = datetime.date(2024, 1, 1)

    comparator_ab = DateComparator(date_a, date_b)
    print(comparator_ab.is_equal())
    print(comparator_ab.get_comparison_result())

    comparator_ac = DateComparator(date_a, date_c)
    print(comparator_ac.is_less_than())
    print(comparator_ac.get_comparison_result())

    comparator_ca = DateComparator(date_c, date_a)
    print(comparator_ca.is_greater_than())
    print(comparator_ca.get_comparison_result())