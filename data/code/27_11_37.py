class ValueComparator:
    def __init__(self, tolerance=1e-10):
        self.tolerance = tolerance

    def are_values_different(self, a, b):
        return abs(a - b) > self.tolerance

if __name__ == '__main__':
    comparator = ValueComparator()
    value1 = 10
    value2 = 10.00000000000001
    result1 = comparator.are_values_different(value1, value2)
    print(result1)

    # Additional test with different tolerance
    comparator.tolerance = 1e-9
    result2 = comparator.are_values_different(value1, value2)
    print(result2)