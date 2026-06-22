class FactorialCalculator:
    def compute(self, n):
        if n < 0:
            raise ValueError("Input must be a non-negative integer")
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

if __name__ == '__main__':
    calc = FactorialCalculator()
    sample_values = [0, 1, 5, 10]
    for val in sample_values:
        print(calc.compute(val))