class PrecisionEqualityChecker:
    DEFAULT_TOLERANCE = 1e-9

    @staticmethod
    def is_within_tolerance(num1, num2, tolerance):
        return abs(num1 - num2) <= tolerance

    def __init__(self, tolerance=None):
        if tolerance is not None and tolerance < 0:
            raise ValueError("Tolerance must be non-negative")
        self.tolerance = tolerance if tolerance is not None else self.DEFAULT_TOLERANCE

    def check_equality(self, num1, num2):
        return self.is_within_tolerance(num1, num2, self.tolerance)

if __name__ == '__main__':
    value1 = 0.1 + 0.2
    value2 = 0.3
    tolerance = 1e-8
    checker = PrecisionEqualityChecker(tolerance)
    result = checker.check_equality(value1, value2)
    print(result)