class LengthComparator:
    DEFAULT_EPSILON = 1e-9

    def __init__(self):
        self.length1 = 5.0
        self.length2 = 5.000000001

    def are_equal_within_epsilon(self, epsilon=DEFAULT_EPSILON):
        return abs(self.length1 - self.length2) < epsilon

    def absolute_difference(self):
        return abs(self.length1 - self.length2)

if __name__ == '__main__':
    comparator = LengthComparator()
    print(comparator.are_equal_within_epsilon())
    print(comparator.absolute_difference())