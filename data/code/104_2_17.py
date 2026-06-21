class TimestampDelta:
    def __init__(self, ts1: int, ts2: int):
        if not isinstance(ts1, int) or not isinstance(ts2, int):
            raise ValueError("Timestamps must be integers")
        self.ts1 = ts1
        self.ts2 = ts2

    def get_seconds(self) -> int:
        return abs(self.ts1 - self.ts2)

if __name__ == '__main__':
    delta = TimestampDelta(1672531200, 1672531260)
    print(delta.get_seconds())