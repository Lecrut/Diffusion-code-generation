from datetime import datetime

class DateTimeComparator:
    def __init__(self, first: datetime, second: datetime):
        self.first = first
        self.second = second

    def compare(self) -> str:
        if self.first < self.second:
            return "First is earlier"
        if self.first > self.second:
            return "Second is earlier"
        return "They are equal"

    def get_difference_seconds(self) -> int:
        delta = self.second - self.first
        return int(delta.total_seconds())

if __name__ == '__main__':
    dt_a = datetime(2024, 5, 10, 8, 30, 0)
    dt_b = datetime(2024, 5, 10, 9, 45, 0)
    comparator = DateTimeComparator(dt_a, dt_b)
    print(comparator.compare())
    print(comparator.get_difference_seconds())