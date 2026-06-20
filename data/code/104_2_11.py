class TimestampComparator:

    @staticmethod
    def compare(timestamp1, timestamp2):
        return abs(timestamp1 - timestamp2)
if __name__ == '__main__':
    comparator = TimestampComparator()
    ts_a = 1673980800
    ts_b = 1672406400
    difference = comparator.compare(ts_a, ts_b)
    print(f'Difference between {ts_a} and {ts_b}: {difference} seconds')