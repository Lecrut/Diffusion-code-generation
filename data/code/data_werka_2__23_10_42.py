class EqualityChecker:
    DEFAULT_TOLERANCE = 1e-9

    def __init__(self, tolerance=None):
        if tolerance is not None and tolerance < 0:
            raise ValueError("Tolerance must be non-negative")
        self.tolerance = tolerance if tolerance is not None else self.DEFAULT_TOLERANCE

    def check_equality(self, num1, num2):
        return abs(num1 - num2) <= self.tolerance

if __name__ == '__main__':
    float_a = 0.7 + 0.3
    float_b = 1.0
    checker = EqualityChecker()
    result = checker.check_equality(float_a, float_b)
    print(result)