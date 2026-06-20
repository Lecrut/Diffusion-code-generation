class LengthComparator:
    def __init__(self):
        self.length_a = 10.0
        self.length_b = 10.0001
        self.epsilon = 0.001

    def are_equal_within_tolerance(self):
        return abs(self.length_a - self.length_b) <= self.epsilon

    def absolute_difference(self):
        return abs(self.length_a - self.length_b)

if __name__ == '__main__':
    comparator = LengthComparator()
    print(comparator.are_equal_within_tolerance())
    print(comparator.absolute_difference())