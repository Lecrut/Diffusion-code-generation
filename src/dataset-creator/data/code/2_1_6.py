class PositiveValueValidator:
    def __init__(self, name: str = "PositiveValueValidator") -> None:
        self.name = name
    def validate(self, value) -> bool:
        if not isinstance(value, (int, float)):
            raise TypeError(f"Expected int or float, got {type(value).__name__}")
        import math
        if math.isnan(value) or math.isinf(value):
            raise ValueError("Value must be a finite number.")
        return value > 0
if __name__ == '__main__':
    validator = PositiveValueValidator()
    test_cases = [42, -10.5, float('nan'), float('-inf'), float('inf')]
    for case in test_cases:
        try:
            result = validator.validate(case)
            print(f"Input {case!r}: Valid positive value -> {result}")
        except (TypeError, ValueError) as e:
            print(f"Input {case!r}: Error - {e.__class__.__name__} ({str(e)})")