from datetime import datetime

class DateTimeComparator:
    def __init__(self, first: datetime, second: datetime):
        self.first = first
        self.second = second

    def get_comparison_result(self) -> str:
        if self.first < self.second:
            return 'First is earlier'
        if self.first > self.second:
            return 'Second is earlier'
        return 'They are equal'

    def get_first(self) -> datetime:
        return self.first

    def get_second(self) -> datetime:
        return self.second

if __name__ == '__main__':
    dt1 = datetime(2023, 1, 1, 12, 0, 0)
    dt2 = datetime(2023, 1, 2, 12, 0, 0)
    comparator = DateTimeComparator(dt1, dt2)
    print(comparator.get_comparison_result())
    print(comparator.get_first())
    print(comparator.get_second())