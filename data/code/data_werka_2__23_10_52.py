class FloatEqualityChecker:
    DEFAULT_TOLERANCE = 1e-9

    def __init__(self, tolerance=None):
        self.tolerance = tolerance if tolerance is not None else self.DEFAULT_TOLERANCE

    def check_equality(self, num1, num2):
        return abs(num1 - num2) <= self.tolerance

if __name__ == '__main__':
    float_value_1 = 0.1 + 0.2
    float_value_2 = 0.3
    checker = FloatEqualityChecker()
    result = checker.check_equality(float_value_1, float_value_2)
    print(result)