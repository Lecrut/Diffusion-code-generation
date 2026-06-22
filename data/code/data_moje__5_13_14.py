class LengthComparator:
    def __init__(self):
        self.length1 = 10.0001
        self.length2 = 10.0002
        self.epsilon = 0.0001

    def are_equal(self, a, b, tolerance=None):
        if tolerance is None:
            tolerance = self.epsilon
        return abs(a - b) <= tolerance

    def absolute_difference(self, a, b):
        return abs(a - b)

if __name__ == '__main__':
    comparator = LengthComparator()
    result_equal = comparator.are_equal(comparator.length1, comparator.length2)
    result_diff = comparator.absolute_difference(comparator.length1, comparator.length2)
    print(f"{result_equal=}")
    print(f"{result_diff=}")