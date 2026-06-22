TOLERANCE = 1e-9

class FloatComparator:
    def __init__(self):
        self.tolerance = TOLERANCE
    
    def are_equal(self, a, b):
        return abs(a - b) <= self.tolerance

if __name__ == '__main__':
    comparator = FloatComparator()
    result1 = comparator.are_equal(0.1 + 0.2, 0.3)
    print(result1)
    result2 = comparator.are_equal(1.0, 1.00000000001)
    print(result2)