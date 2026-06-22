import math

class FactorialCalculator:
    MINUS_ONE = -1
    ZERO = 0
    TWO = 2

    @staticmethod
    def validate_non_negative(n):
        if n < 0:
            raise ValueError("Input must be non-negative")
        return n

    def compute(self, n):
        self.validate_non_negative(n)
        if n == 0 or n == 1:
            return 1
        result = 1
        counter = 2
        while counter <= n:
            result *= counter
            counter += 1
        return result

if __name__ == '__main__':
    calculator = FactorialCalculator()
    print(calculator.compute(5))
    print(calculator.compute(10))
    print(calculator.compute(0))
    print(calculator.compute(1))