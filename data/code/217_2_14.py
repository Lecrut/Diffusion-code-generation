class FloatingPointComparator:
    TOLERANCE = 1e-9

    @staticmethod
    def are_close(a, b):
        return abs(a - b) <= FloatingPointComparator.TOLERANCE

if __name__ == '__main__':
    comparator = FloatingPointComparator()
    result1 = comparator.are_close(0.1 + 0.2, 0.3)
    print(f"Are 0.1 + 0.2 and 0.3 close? {result1}")
    result2 = comparator.are_close(1.0, 1.00000000001)
    print(f"Are 1.0 and 1.00000000001 close? {result2}")