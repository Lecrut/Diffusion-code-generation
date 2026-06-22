TOLERANCE = 1e-9

class FloatingPointComparator:
    def __init__(self):
        self.tolerance = TOLERANCE
    
    def are_equal(self, a, b):
        return abs(a - b) <= self.tolerance

if __name__ == '__main__':
    comparator = FloatingPointComparator()
    result1 = comparator.are_equal(0.1 + 0.2, 0.3)
    print(f"Comparing 0.1 + 0.2 and 0.3: {result1}")
    result2 = comparator.are_equal(1.0, 1.00000000001)
    print(f"Comparing 1.0 and 1.00000000001: {result2}")