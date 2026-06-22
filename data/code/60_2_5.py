class FactorialCalculator:
    def compute(self, n):
        if n < 0:
            raise ValueError("n must be non-negative")
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

if __name__ == '__main__':
    calculator = FactorialCalculator()
    sample_values = [0, 1, 5, 10]
    for value in sample_values:
        print(calculator.compute(value))