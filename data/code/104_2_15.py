class TimestampComparator:
    EPOCH = 0

    @staticmethod
    def compare(timestamp1: int, timestamp2: int) -> int:
        return abs(timestamp1 - timestamp2)
if __name__ == '__main__':
    comparator = TimestampComparator()
    ts_a = 1673836800
    ts_b = 1672966400
    result1 = comparator.compare(ts_a, ts_b)
    print(f'Comparing {ts_a} and {ts_b}: {result1}')