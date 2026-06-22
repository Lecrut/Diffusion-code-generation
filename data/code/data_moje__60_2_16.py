class FactorialCalculator:
    def compute(self, n):
        if n < 0:
            raise ValueError("Negative input is not allowed")
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

if __name__ == '__main__':
    calculator = FactorialCalculator()
    print(calculator.compute(5))
    print(calculator.compute(10))