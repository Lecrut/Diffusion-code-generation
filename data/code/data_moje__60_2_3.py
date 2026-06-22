class FactorialCalculator:
    def __init__(self):
        self.cache = {0: 1}

    def compute(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if n in self.cache:
            return self.cache[n]
        result = 1
        for i in range(1, n + 1):
            result *= i
            self.cache[i] = result
        return result

if __name__ == '__main__':
    calculator = FactorialCalculator()
    sample_values = [0, 1, 5, 10, 20]
    for val in sample_values:
        print(calculator.compute(val))