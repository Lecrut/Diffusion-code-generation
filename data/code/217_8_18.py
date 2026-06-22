import math

class DecimalComparator:
    def __init__(self, epsilon=1e-09):
        self.epsilon = epsilon

    def are_decimals_equal(self, a, b):
        if math.isnan(a) or math.isnan(b):
            return a == b
        if math.isinf(a) or math.isinf(b):
            return a == b
        return abs(a - b) <= self.epsilon

if __name__ == '__main__':
    comparator = DecimalComparator()
    print(comparator.are_decimals_equal(0.1 + 0.2, 0.3))
    print(comparator.are_decimals_equal(float('nan'), float('nan')))
    print(comparator.are_decimals_equal(float('inf'), float('inf')))
    print(comparator.are_decimals_equal(float('-inf'), float('-inf')))
    print(comparator.are_decimals_equal(float('inf'), float('-inf')))