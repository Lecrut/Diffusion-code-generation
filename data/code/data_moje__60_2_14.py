class FactorialCalculator:
    def __init__(self):
        self._cache = {0: 1, 1: 1}

    def compute_factorial(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if n in self._cache:
            return self._cache[n]
        result = 1
        for i in range(2, n + 1):
            result *= i
            self._cache[i] = result
        return result

if __name__ == '__main__':
    calculator = FactorialCalculator()
    sample_values = [0, 1, 5, 10, 15]
    for value in sample_values:
        print(calculator.compute_factorial(value))