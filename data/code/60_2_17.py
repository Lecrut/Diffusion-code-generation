class FactorialCalculator:
    def compute(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

if __name__ == '__main__':
    calculator = FactorialCalculator()
    sample_values = [5, 10, 0]
    for value in sample_values:
        result = calculator.compute(value)
        print(result)