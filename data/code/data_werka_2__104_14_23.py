import datetime

class DateComparator:
    def __init__(self, first_date: datetime.date, second_date: datetime.date):
        self._first = first_date
        self._second = second_date

    @property
    def first_date(self) -> datetime.date:
        return self._first

    @property
    def second_date(self) -> datetime.date:
        return self._second

    def equals(self) -> bool:
        return self._first == self._second

    def is_greater(self) -> bool:
        return self._first > self._second

    def is_less(self) -> bool:
        return self._first < self._second

    def compare(self) -> int:
        if self._first < self._second:
            return -1
        if self._first > self._second:
            return 1
        return 0

if __name__ == '__main__':
    d1 = datetime.date(2023, 10, 15)
    d2 = datetime.date(2023, 10, 15)
    comparator = DateComparator(d1, d2)
    print(comparator.equals())
    print(comparator.compare())

    d3 = datetime.date(2024, 1, 1)
    d4 = datetime.date(2023, 12, 31)
    comparator2 = DateComparator(d3, d4)
    print(comparator2.is_greater())
    print(comparator2.is_less())
    print(comparator2.compare())