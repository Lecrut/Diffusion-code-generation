class ValueComparator:
    def __init__(self, epsilon=1e-10):
        self.epsilon = epsilon

    def are_values_different(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both values must be either int or float.")
        return abs(a - b) > self.epsilon

if __name__ == '__main__':
    value1 = 10
    value2 = 10.00000000000001
    comparator = ValueComparator()
    result = comparator.are_values_different(value1, value2)
    print(result)