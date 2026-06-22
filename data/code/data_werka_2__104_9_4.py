class TimestampComparator:
    def __init__(self, first: float, second: float):
        self.first = first
        self.second = second

    def is_first_before_second(self) -> bool:
        return self.first < self.second

if __name__ == '__main__':
    comp = TimestampComparator(1609459200.0, 1609459201.0)
    print(comp.is_first_before_second())
    comp2 = TimestampComparator(1609459201.0, 1609459200.0)
    print(comp2.is_first_before_second())