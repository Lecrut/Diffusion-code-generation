class FactorialCalculator:
    def compute(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

if __name__ == '__main__':
    calculator = FactorialCalculator()
    print(calculator.compute(5))
    print(calculator.compute(10))
    print(calculator.compute(0))