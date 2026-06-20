class FloatComparator:
    def __init__(self, epsilon: float = 1e-9):
        self.epsilon = epsilon

    def is_zero(self, value: float) -> bool:
        return abs(value) < self.epsilon

if __name__ == '__main__':
    comparator = FloatComparator(epsilon=1e-7)
    test_values = [0.0, 1e-8, -1e-8, 1e-6, -1e-6]
    results = {val: comparator.is_zero(val) for val in test_values}
    print(results)