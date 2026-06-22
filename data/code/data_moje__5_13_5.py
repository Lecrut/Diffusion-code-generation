import math

class LengthComparator:
    def __init__(self):
        self.value1 = 1.000000001
        self.value2 = 1.000000002
        self.epsilon = 1e-9

    def are_equal_within_epsilon(self):
        return math.fabs(self.value1 - self.value2) <= self.epsilon

    def get_absolute_difference(self):
        return math.fabs(self.value1 - self.value2)

if __name__ == '__main__':
    comparator = LengthComparator()
    print(comparator.are_equal_within_epsilon())
    print(comparator.get_absolute_difference())