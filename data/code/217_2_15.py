class FloatingPointComparer:
    def __init__(self, tolerance=1e-9):
        self.tolerance = tolerance

    def are_equal(self, a, b):
        return abs(a - b) <= self.tolerance

if __name__ == '__main__':
    comparer = FloatingPointComparer()
    result1 = comparer.are_equal(0.1 + 0.2, 0.3)
    print(result1)
    result2 = comparer.are_equal(1.0, 1.00000000001)
    print(result2)