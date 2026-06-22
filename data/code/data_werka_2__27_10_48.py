class NumericalComparator:
    def __init__(self, tolerance=1e-10):
        self.tolerance = tolerance

    def compare(self, value1, value2):
        return abs(value1 - value2) > self.tolerance

if __name__ == '__main__':
    value1 = 10
    value2 = 10.00000000000001
    comparator = NumericalComparator()
    
    result = comparator.compare(value1, value2)
    print(result)  # Should print True

    # Additional test cases
    value3 = 10.0
    value4 = 10.00000000000001
    print(comparator.compare(value3, value4))  # Should print True

    value5 = 10.0
    value6 = 10.0
    print(comparator.compare(value5, value6))  # Should print False