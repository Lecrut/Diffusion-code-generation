class FactorialCalculator:
    def compute_factorial(self, n):
        if n < 0:
            raise ValueError("Negative numbers are not allowed")
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

if __name__ == '__main__':
    calculator = FactorialCalculator()
    print(calculator.compute_factorial(5))
    print(calculator.compute_factorial(10))