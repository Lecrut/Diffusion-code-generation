import math

class LengthComparator:
    def __init__(self):
        self.value_a = 10.00000001
        self.value_b = 10.00000000
    
    def is_equal_with_epsilon(self, epsilon=1e-9):
        return abs(self.value_a - self.value_b) < epsilon
    
    def absolute_difference(self):
        return abs(self.value_a - self.value_b)

if __name__ == '__main__':
    comparator = LengthComparator()
    print(comparator.absolute_difference())
    print(comparator.is_equal_with_epsilon())