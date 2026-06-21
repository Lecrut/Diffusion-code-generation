from datetime import datetime

class DateComparator:
    def __init__(self, date_a: datetime, date_b: datetime):
        self.date_a = date_a
        self.date_b = date_b

    def is_first_earlier(self) -> bool:
        return self.date_a < self.date_b

    def is_second_earlier(self) -> bool:
        return self.date_b < self.date_a

    def are_equal(self) -> bool:
        return self.date_a == self.date_b

if __name__ == '__main__':
    start = datetime(2020, 6, 15, 10, 0, 0)
    end = datetime(2020, 6, 15, 11, 0, 0)
    comparator = DateComparator(start, end)
    print(comparator.is_first_earlier())
    print(comparator.is_second_earlier())
    print(comparator.are_equal())