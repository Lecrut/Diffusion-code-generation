import datetime

class DateComparator:
    def __init__(self, first_date, second_date):
        self._first = first_date
        self._second = second_date

    def is_equal(self):
        return self._first == self._second

    def is_greater_than(self):
        return self._first > self._second

    def is_less_than(self):
        return self._first < self._second

    def get_relationship(self):
        if self._first == self._second:
            return "equal"
        if self._first > self._second:
            return "greater"
        return "less"

if __name__ == '__main__':
    date_a = datetime.date(2023, 10, 15)
    date_b = datetime.date(2023, 10, 15)
    comparator = DateComparator(date_a, date_b)
    print(comparator.is_equal())
    print(comparator.get_relationship())