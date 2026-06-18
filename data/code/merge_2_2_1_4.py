class PositiveValueValidator:
    def __init__(self) -> None:
        pass
    @staticmethod
    def validate(value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Expected numeric type, got {type(value).__name__}")
        import math
        if not math.isfinite(value):
            sign = "positive or negative infinity" if value != 0 else "zero"
            raise ValueError(f"Value is NaN{sign}.")
        return value > 0
if __name__ == '__main__':
    validator = PositiveValueValidator()
    test_cases = [1, -5.2, float('inf'), float('-inf'), float('nan')]
    for case in test_cases:
        try:
            result = validator.validate(case)
            print(f"Input {case!r} -> Result: {result}")
        except (TypeError, ValueError) as e:
            print(f"Input {case!r} -> Error: {e.__class__.__name__}: {e}")