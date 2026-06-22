class LengthComparator:
    def __init__(self):
        self.length1 = 10.0
        self.length2 = 10.0001

    def are_equal_within_epsilon(self, epsilon=1e-5):
        return abs(self.length1 - self.length2) < epsilon

    def absolute_difference(self):
        return abs(self.length1 - self.length2)

if __name__ == '__main__':
    comparator = LengthComparator()
    print(comparator.are_equal_within_epsilon())
    print(comparator.absolute_difference())