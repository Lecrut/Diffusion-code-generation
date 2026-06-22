class FloatingPointComparator:
    DEFAULT_TOLERANCE = 1e-9

    def __init__(self, tolerance=None):
        if tolerance is not None and tolerance < 0:
            raise ValueError("Tolerance must be non-negative")
        self.tolerance = tolerance if tolerance is not None else self.DEFAULT_TOLERANCE

    def compare(self, num1, num2):
        return abs(num1 - num2) <= self.tolerance

if __name__ == '__main__':
    sample_value_1 = 0.7 + 0.3
    sample_value_2 = 1.0
    comparator = FloatingPointComparator()
    result = comparator.compare(sample_value_1, sample_value_2)
    print(result)