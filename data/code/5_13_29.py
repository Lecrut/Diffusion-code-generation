class LengthComparator:

    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def are_equal_within_epsilon(self, epsilon=0.0001):
        return abs(self.length1 - self.length2) < epsilon

    def absolute_difference(self):
        return abs(self.length1 - self.length2)
if __name__ == '__main__':
    comparator = LengthComparator(10.0002, 10.0001)
    print(comparator.are_equal_within_epsilon())
    print(comparator.absolute_difference())