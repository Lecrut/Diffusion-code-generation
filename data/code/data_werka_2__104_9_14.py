class TimestampComparator:
    def __init__(self, first: float, second: float):
        self.first = first
        self.second = second

    def is_first_before_second(self) -> bool:
        return self.first < self.second

if __name__ == '__main__':
    comparator = TimestampComparator(1700000000.0, 1700000001.0)
    result = comparator.is_first_before_second()
    print(result)
    earlier_comparator = TimestampComparator(1700000002.0, 1700000001.0)
    earlier_result = earlier_comparator.is_first_before_second()
    print(earlier_result)