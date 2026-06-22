class NumberComparator:
    def __init__(self, tolerance=1e-9):
        self.tolerance = tolerance

    def are_equal(self, a, b):
        return abs(a - b) <= self.tolerance

if __name__ == '__main__':
    comparator = NumberComparator()
    result1 = comparator.are_equal(0.1 + 0.2, 0.3)
    print(f"Are 0.1 + 0.2 and 0.3 equal? {result1}")
    result2 = comparator.are_equal(1.0, 1.00000000001)
    print(f"Are 1.0 and 1.00000000001 equal? {result2}")