class FloatComparator:
    TOLERANCE = 1e-09

    @staticmethod
    def compare(a, b):
        if abs(a - b) < FloatComparator.TOLERANCE:
            return 'equal'
        elif a > b:
            return 'a'
        else:
            return 'b'
if __name__ == '__main__':
    comparator = FloatComparator()
    result1 = comparator.compare(0.1 + 0.2, 0.3)
    print(result1)
    result2 = comparator.compare(1.000000001, 1.0)
    print(result2)