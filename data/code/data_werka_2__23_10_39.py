class PrecisionComparator:
    DEFAULT_TOLERANCE = 1e-09

    def __init__(self, tolerance=None):
        if tolerance is not None and tolerance < 0:
            raise ValueError('Tolerance must be non-negative')
        self.tolerance = tolerance if tolerance is not None else self.DEFAULT_TOLERANCE

    def compare(self, num1, num2):
        return abs(num1 - num2) <= self.tolerance

    def set_tolerance(self, new_tolerance):
        if new_tolerance < 0:
            raise ValueError('Tolerance must be non-negative')
        self.tolerance = new_tolerance
if __name__ == '__main__':
    float_value1 = 0.1 + 0.2
    float_value2 = 0.3
    comparator = PrecisionComparator()
    result_default = comparator.compare(float_value1, float_value2)
    print('Comparison with default tolerance:', result_default)
    new_tolerance = 1e-08
    comparator.set_tolerance(new_tolerance)
    result_new_tolerance = comparator.compare(float_value1, float_value2)
    print('Comparison with new tolerance:', result_new_tolerance)