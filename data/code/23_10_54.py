class PrecisionChecker:
    DEFAULT_TOLERANCE = 1e-9

    def __init__(self, tolerance=None):
        if tolerance is not None and tolerance < 0:
            raise ValueError("Tolerance must be non-negative")
        self.tolerance = tolerance if tolerance is not None else self.DEFAULT_TOLERANCE

    def check_equality(self, num1, num2):
        return abs(num1 - num2) <= self.tolerance

if __name__ == '__main__':
    SAMPLE_FLOAT_1 = 0.1 + 0.2
    SAMPLE_FLOAT_2 = 0.3
    checker = PrecisionChecker()
    result = checker.check_equality(SAMPLE_FLOAT_1, SAMPLE_FLOAT_2)
    print(result)