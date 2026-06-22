class FloatingPointComparator:
    TOLERANCE = 1e-9

    @staticmethod
    def are_equal(a, b):
        return abs(a - b) <= FloatingPointComparator.TOLERANCE

if __name__ == '__main__':
    comparator = FloatingPointComparator()
    result1 = comparator.are_equal(0.1 + 0.2, 0.3)
    print(result1)
    result2 = comparator.are_equal(1.0, 1.00000000001)
    print(result2)