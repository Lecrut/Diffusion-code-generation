class LengthComparator:
    def __init__(self):
        self.length1 = 10.0001
        self.length2 = 10.0002
        self.epsilon = 0.00005

    def are_equal_within_epsilon(self):
        difference = abs(self.length1 - self.length2)
        return difference <= self.epsilon

    def absolute_difference(self):
        return abs(self.length1 - self.length2)

if __name__ == '__main__':
    comparator = LengthComparator()
    print(comparator.are_equal_within_epsilon())
    print(comparator.absolute_difference())