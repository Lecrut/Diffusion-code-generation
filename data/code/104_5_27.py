from datetime import datetime

class DateTimeComparator:
    def __init__(self, first: datetime, second: datetime):
        if not isinstance(first, datetime):
            raise ValueError("first must be a datetime instance")
        if not isinstance(second, datetime):
            raise ValueError("second must be a datetime instance")
        self.first = first
        self.second = second

    def get_comparison_result(self) -> str:
        if self.first < self.second:
            return "First is earlier"
        if self.first > self.second:
            return "Second is earlier"
        return "They are equal"

def compare_datetimes(first: datetime, second: datetime) -> str:
    comparator = DateTimeComparator(first, second)
    return comparator.get_comparison_result()

if __name__ == '__main__':
    dt_a = datetime(2024, 5, 10, 8, 30, 0)
    dt_b = datetime(2024, 5, 10, 8, 30, 0)
    output = compare_datetimes(dt_a, dt_b)
    print(output)