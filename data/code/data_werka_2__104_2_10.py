class TimestampDiffCalculator:
    _MIN_INPUT = 0
    _MAX_INPUT = 2**63 - 1

    @staticmethod
    def _validate(ts: int) -> int:
        if not isinstance(ts, int) or isinstance(ts, bool):
            raise ValueError("Timestamp must be an integer")
        if ts < TimestampDiffCalculator._MIN_INPUT or ts > TimestampDiffCalculator._MAX_INPUT:
            raise ValueError("Timestamp out of valid range")
        return ts

    @classmethod
    def calculate_difference(cls, ts1: int, ts2: int) -> int:
        validated_ts1 = cls._validate(ts1)
        validated_ts2 = cls._validate(ts2)
        return abs(validated_ts1 - validated_ts2)

if __name__ == '__main__':
    calculator = TimestampDiffCalculator()
    result = calculator.calculate_difference(1672531200, 1672531260)
    print(result)