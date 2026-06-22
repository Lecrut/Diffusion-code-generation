class EpsilonComparator:
    DEFAULT_EPSILON = 1e-10

    def __init__(self, epsilon=None):
        self.epsilon = epsilon if epsilon is not None else self.DEFAULT_EPSILON

    def compare(self, a, b):
        return abs(a - b) > self.epsilon

if __name__ == '__main__':
    value1 = 10
    value2 = 10.00000000000001
    comparator = EpsilonComparator()
    
    result_default_epsilon = comparator.compare(value1, value2)
    print(f"Using default epsilon: {result_default_epsilon}")
    
    custom_epsilon_comparator = EpsilonComparator(epsilon=1e-5)
    result_custom_epsilon = custom_epsilon_comparator.compare(value1, value2)
    print(f"Using custom epsilon (1e-5): {result_custom_epsilon}")