class EqualityChecker:
    DEFAULT_TOLERANCE = 1e-9

    @staticmethod
    def compare(num1, num2, tolerance=None):
        if tolerance is None:
            tolerance = EqualityChecker.DEFAULT_TOLERANCE
        return abs(num1 - num2) <= tolerance

if __name__ == '__main__':
    value1 = 0.1 + 0.2
    value2 = 0.3
    result = EqualityChecker.compare(value1, value2)
    print(result)