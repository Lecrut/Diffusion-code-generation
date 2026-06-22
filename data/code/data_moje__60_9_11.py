class FactorialCalculator:
    def __init__(self):
        self.history = []

    def compute(self, n):
        if n < 0:
            raise ValueError("Input must be non-negative")
        result = 1
        multiplier = 2
        while multiplier <= n:
            result *= multiplier
            multiplier += 1
        self.history.append((n, result))
        return result

    def get_last_computed(self):
        if not self.history:
            return None
        return self.history[-1]

if __name__ == '__main__':
    calculator = FactorialCalculator()
    print(calculator.compute(0))
    print(calculator.compute(1))
    print(calculator.compute(5))
    print(calculator.compute(10))
    print(calculator.get_last_computed())