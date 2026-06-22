class EqualityChecker:
    DEFAULT_TOLERANCE = 1e-9

    def __init__(self, tolerance=None):
        self.tolerance = tolerance if tolerance is not None else self.DEFAULT_TOLERANCE

    def check_equality(self, num1, num2):
        return abs(num1 - num2) <= self.tolerance

if __name__ == '__main__':
    sample_values = {
        'a': 0.1 + 0.2,
        'b': 0.3
    }
    checker = EqualityChecker()
    result = checker.check_equality(sample_values['a'], sample_values['b'])
    print(result)