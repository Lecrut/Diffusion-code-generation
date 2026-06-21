class TimestampComparator:
    UNIT_SECONDS = 1

    @staticmethod
    def _validate_integer(value: int) -> bool:
        return isinstance(value, int)

    def calculate_absolute_difference(self, timestamp_a: int, timestamp_b: int) -> int:
        if not self._validate_integer(timestamp_a):
            raise ValueError("timestamp_a must be an integer")
        if not self._validate_integer(timestamp_b):
            raise ValueError("timestamp_b must be an integer")
        delta = timestamp_a - timestamp_b
        if delta < 0:
            return -delta
        return delta

if __name__ == '__main__':
    comparator = TimestampComparator()
    ts_a = 1672531200
    ts_b = 1672531500
    result = comparator.calculate_absolute_difference(ts_a, ts_b)
    print(result)