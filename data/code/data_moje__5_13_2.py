class LengthComparator:
    def __init__(self):
        self.length1 = 10.0
        self.length2 = 10.0001

    def are_equal_within_tolerance(self, epsilon):
        return abs(self.length1 - self.length2) <= epsilon

    def get_absolute_difference(self):
        return abs(self.length1 - self.length2)

if __name__ == '__main__':
    comparator = LengthComparator()
    print(comparator.are_equal_within_tolerance(0.001))
    print(comparator.get_absolute_difference())