class TimestampComparator:
    def compare(self, timestamp1, timestamp2):
        return abs(timestamp1 - timestamp2)

if __name__ == '__main__':
    comparator = TimestampComparator()
    ts_a = 1673942400
    ts_b = 1672310400
    result = comparator.compare(ts_a, ts_b)
    print(f'Difference between {ts_a} and {ts_b}: {result} seconds')