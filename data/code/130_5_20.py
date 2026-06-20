def is_zero(value: float, epsilon: float = 1e-9) -> bool:
    return abs(value) < epsilon

class ZeroChecker:
    def __init__(self, epsilon: float = 1e-9):
        self.epsilon = epsilon
    
    def check(self, value: float) -> bool:
        return is_zero(value, self.epsilon)

if __name__ == '__main__':
    checker = ZeroChecker(epsilon=1e-7)
    test_values = [0.0, 1e-8, -1e-8, 1e-6, -1e-6]
    results = {val: checker.check(val) for val in test_values}
    print(results)