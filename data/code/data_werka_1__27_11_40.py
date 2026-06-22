class ValueComparer:
    def __init__(self, tolerance=1e-10):
        if not isinstance(tolerance, (int, float)) or tolerance < 0:
            raise ValueError("Tolerance must be a non-negative number.")
        self.tolerance = tolerance

    def are_values_different(self, a, b):
        return abs(a - b) > self.tolerance

if __name__ == '__main__':
    comparer = ValueComparer()
    value1 = 10
    value2 = 10.00000000000001
    result = comparer.are_values_different(value1, value2)
    print(result)