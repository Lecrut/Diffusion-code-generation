import math
class PositiveValueValidator:
    def __init__(self):
        pass
    def is_positive(self, value) -> bool:
        if isinstance(value, (int, float)):
            return math.isnan(value) or math.isinf(value) or value <= 0
        else:
            raise TypeError("Input must be an integer or float.")
if __name__ == '__main__':
    validator = PositiveValueValidator()
    test_cases = [1.5, -3, 0, float('nan'), float('inf'), float('-inf')]
    for case in test_cases:
        try:
            result = validator.is_positive(case)
            print(f"Input {case}: Is positive? {result}")
        except TypeError as e:
            print(f"Input {case}: Error - {e}")