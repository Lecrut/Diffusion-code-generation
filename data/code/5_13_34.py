class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def is_equal_within_tolerance(self, epsilon=1e-9):
        return abs(self.length1 - self.length2) < epsilon

    def absolute_difference(self):
        return abs(self.length1 - self.length2)

if __name__ == '__main__':
    comparator = LengthComparator(1.000000001, 1.0)
    print(comparator.is_equal_within_tolerance())
    print(comparator.absolute_difference())