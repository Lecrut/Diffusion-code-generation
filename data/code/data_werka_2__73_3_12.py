class TimestampDiff:
    def __init__(self, t1, t2):
        if not isinstance(t1, (int, float)):
            raise ValueError("t1 must be numeric")
        if not isinstance(t2, (int, float)):
            raise ValueError("t2 must be numeric")
        self.t1 = t1
        self.t2 = t2

    def get_difference(self):
        return abs(self.t1 - self.t2)

if __name__ == '__main__':
    ts1 = 1700000000
    ts2 = 1700003600
    diff = TimestampDiff(ts1, ts2)
    print(diff.get_difference())