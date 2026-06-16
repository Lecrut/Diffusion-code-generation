class PositiveValueValidator:
    def __init__(self, name: str) -> None:
        self.name = name
    def validate(self, value: float | int) -> bool:
        import math
        if not isinstance(value, (int, float)):
            raise TypeError(f"Expected numeric type, got {type(value).__name__}")
        if value != value:                  
            return False
        import math
        if math.isinf(value):
            return False
        return value > 0
if __name__ == '__main__':
    validator = PositiveValueValidator("Sample")
    test_cases = [1, -5.5, float('nan'), float('-inf'), float('inf'), "string", True]
    for case in test_cases:
        try:
            result = validator.validate(case)
            print(f"Input {case!r}: Validated as {'Positive' if result else 'Not Positive'}")
        except TypeError as e:
            print(f"Input {case!r}: Error - {e}")