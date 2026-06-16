class PositiveValueValidator:
    def validate(self, value):
        import math
        if not isinstance(value, (int, float)):
            raise TypeError(f"Expected int or float, got {type(value).__name__}")
        if math.isnan(value):
            return False
        try:
            result = value > 0
            if math.isinf(value):
                return False
            return result
        except TypeError:
            return False
if __name__ == '__main__':
    validator = PositiveValueValidator()
    test_cases = [42, -5, 0, float('nan'), float('-inf'), float('inf')]
    for case in test_cases:
        result = validator.validate(case)
        print(f"Input: {case} -> Is positive: {result}")