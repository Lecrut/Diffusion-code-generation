class LengthComparator:

    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def are_equal_within_epsilon(self, epsilon=1e-09):
        return abs(self.length1 - self.length2) < epsilon

    def absolute_difference(self):
        return abs(self.length1 - self.length2)
if __name__ == '__main__':
    length_comparator = LengthComparator(3.0, 3.000000001)
    print(length_comparator.are_equal_within_epsilon())
    print(length_comparator.absolute_difference())