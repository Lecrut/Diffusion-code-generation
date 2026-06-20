class TimestampComparator:
    def __init__(self, ts1: float, ts2: float):
        self.ts1 = ts1
        self.ts2 = ts2

    def is_before(self) -> bool:
        return self.ts1 < self.ts2

if __name__ == '__main__':
    comparator1 = TimestampComparator(1633075200.0, 1633082400.0)
    print(comparator1.is_before())

    comparator2 = TimestampComparator(1633072800.0, 1633072805.0)
    print(comparator2.is_before())