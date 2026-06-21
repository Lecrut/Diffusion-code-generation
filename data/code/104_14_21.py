import datetime

class DateComparator:
    _COMPARISON_RESULT = {"less": -1, "equal": 0, "greater": 1}

    def __init__(self, date_a: datetime.date, date_b: datetime.date):
        if not isinstance(date_a, datetime.date) or not isinstance(date_b, datetime.date):
            raise ValueError("Inputs must be datetime.date instances")
        self._date_a = date_a
        self._date_b = date_b

    @property
    def date_a(self):
        return self._date_a

    @property
    def date_b(self):
        return self._date_b

    def is_equal(self) -> bool:
        return self._date_a == self._date_b

    def is_greater_than(self) -> bool:
        return self._date_a > self._date_b

    def is_less_than(self) -> bool:
        return self._date_a < self._date_b

    def compare(self) -> int:
        if self._date_a < self._date_b:
            return self._COMPARISON_RESULT["less"]
        if self._date_a == self._date_b:
            return self._COMPARISON_RESULT["equal"]
        return self._COMPARISON_RESULT["greater"]

    def __eq__(self, other):
        if not isinstance(other, DateComparator):
            return NotImplemented
        return self._date_a == other._date_a and self._date_b == other._date_b

    def __hash__(self):
        return hash((self._date_a, self._date_b))

if __name__ == '__main__':
    date_obj_1 = datetime.date(2023, 10, 15)
    date_obj_2 = datetime.date(2023, 10, 15)
    date_obj_3 = datetime.date(2023, 10, 10)

    comparator = DateComparator(date_obj_1, date_obj_2)
    print(comparator.is_equal())
    print(comparator.is_greater_than())
    print(comparator.is_less_than())
    print(comparator.compare())

    comparator_diff = DateComparator(date_obj_1, date_obj_3)
    print(comparator_diff.compare())
    print(comparator_diff.is_greater_than())