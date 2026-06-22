class FactorialCalculator:
    def __init__(self):
        self._base_cases = {0: 1, 1: 1}

    def _validate(self, n):
        if not isinstance(n, int):
            raise TypeError("Input must be an integer")
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        return n

    def calculate(self, n):
        if n in self._base_cases:
            return self._base_cases[n]
        
        if n in self._base_cases:
            return self._base_cases[n]
        
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def compute_factorial(n):
    calculator = FactorialCalculator()
    validated_n = calculator._validate(n)
    return calculator.calculate(validated_n)

if __name__ == '__main__':
    test_inputs = [0, 1, 5, 10, 25]
    for val in test_inputs:
        print(compute_factorial(val))