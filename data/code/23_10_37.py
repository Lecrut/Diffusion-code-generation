class FloatComparator:
    DEFAULT_TOLERANCE = 1e-9

    def __init__(self, tolerance=None):
        self.tolerance = tolerance if tolerance is not None else self.DEFAULT_TOLERANCE

    def are_equal(self, num1, num2):
        return abs(num1 - num2) <= self.tolerance

if __name__ == '__main__':
    float_values = {
        'value1': 0.1 + 0.2,
        'value2': 0.3
    }
    
    comparator = FloatComparator()
    result = comparator.are_equal(float_values['value1'], float_values['value2'])
    print(result)