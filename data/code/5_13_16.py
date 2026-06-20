class LengthComparator:
    def __init__(self):
        self.length_a = 10.0
        self.length_b = 10.001

    def are_equal_within_epsilon(self, epsilon=0.01):
        return abs(self.length_a - self.length_b) <= epsilon

    def absolute_difference(self):
        return abs(self.length_a - self.length_b)

if __name__ == '__main__':
    comparator = LengthComparator()
    print(comparator.are_equal_within_epsilon(0.01))
    print(comparator.absolute_difference())