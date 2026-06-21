class TimestampComparator:
    SECONDS_IN_MINUTE = 60
    SECONDS_IN_HOUR = 3600
    SECONDS_IN_DAY = 86400

    @staticmethod
    def _validate_input(value) -> int:
        if not isinstance(value, int):
            raise ValueError("Input must be an integer timestamp")
        return value

    @classmethod
    def get_seconds_difference(cls, ts_a: int, ts_b: int) -> int:
        validated_a = cls._validate_input(ts_a)
        validated_b = cls._validate_input(ts_b)
        return abs(validated_a - validated_b)

if __name__ == '__main__':
    ts_a = 1700000000
    ts_b = 1699999940
    diff = TimestampComparator.get_seconds_difference(ts_a, ts_b)
    print(diff)