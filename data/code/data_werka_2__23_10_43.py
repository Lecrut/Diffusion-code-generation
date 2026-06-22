class FloatEqualityChecker:
    DEFAULT_TOLERANCE = 1e-9

    def __init__(self, tolerance=None):
        if tolerance is not None and tolerance < 0:
            raise ValueError("Tolerance must be non-negative")
        self.tolerance = tolerance if tolerance is not None else self.DEFAULT_TOLERANCE

    def check_equality(self, num1, num2):
        return abs(num1 - num2) <= self.tolerance

    def set_tolerance(self, new_tolerance):
        if new_tolerance < 0:
            raise ValueError("Tolerance must be non-negative")
        self.tolerance = new_tolerance
        return self

if __name__ == '__main__':
    float_value1 = 0.1 + 0.2
    float_value2 = 0.3
    tolerance_value = 1e-10

    comparator = FloatEqualityChecker(tolerance=tolerance_value)
    
    result_default = comparator.check_equality(float_value1, float_value2)
    print('Comparison with custom tolerance:', result_default)

    comparator.set_tolerance(FloatEqualityChecker.DEFAULT_TOLERANCE)
    result_default_tolerance = comparator.check_equality(float_value1, float_value2)
    print('Comparison with default tolerance:', result_default_tolerance)