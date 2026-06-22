class ToleranceBasedComparator:
    DEFAULT_TOLERANCE = 1e-9

    def __init__(self, tolerance=None):
        if tolerance is not None and tolerance < 0:
            raise ValueError("Tolerance must be non-negative")
        self.tolerance = tolerance if tolerance is not None else self.DEFAULT_TOLERANCE

    def compare(self, num1, num2):
        return abs(num1 - num2) <= self.tolerance

if __name__ == '__main__':
    float_value1 = 0.1 + 0.2
    float_value2 = 0.3
    comparator = ToleranceBasedComparator()
    result = comparator.compare(float_value1, float_value2)
    print(result)