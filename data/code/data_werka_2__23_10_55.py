class FloatEqualityChecker:
    DEFAULT_TOLERANCE = 1e-09

    def __init__(self, tolerance=None):
        if tolerance is not None and tolerance < 0:
            raise ValueError('Tolerance must be non-negative')
        self.tolerance = tolerance if tolerance is not None else self.DEFAULT_TOLERANCE

    def check_equality(self, num1, num2):
        return abs(num1 - num2) <= self.tolerance
if __name__ == '__main__':
    value_a = 0.5 + 0.3
    value_b = 0.8
    equality_checker = FloatEqualityChecker()
    are_equal = equality_checker.check_equality(value_a, value_b)
    print(are_equal)