class FactorialCalculator:
    def __init__(self):
        self.cache = {}

    def compute(self, n):
        if n < 0:
            raise ValueError("n must be non-negative")
        if n in self.cache:
            return self.cache[n]
        result = 1
        for i in range(2, n + 1):
            result *= i
        self.cache[n] = result
        return result

if __name__ == '__main__':
    calc = FactorialCalculator()
    sample_values = [0, 1, 5, 10]
    for value in sample_values:
        print(calc.compute(value))