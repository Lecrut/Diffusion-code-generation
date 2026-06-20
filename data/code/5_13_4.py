class LengthComparator:
    def __init__(self):
        self.length1 = 10.0
        self.length2 = 10.0000001
        self.epsilon = 0.000001

    def are_equal_within_tolerance(self):
        return abs(self.length1 - self.length2) < self.epsilon

    def absolute_difference(self):
        return abs(self.length1 - self.length2)

if __name__ == '__main__':
    comparator = LengthComparator()
    print(comparator.are_equal_within_tolerance())
    print(comparator.absolute_difference())