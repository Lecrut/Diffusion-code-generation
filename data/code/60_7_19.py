class FactorialCalculator:
    MIN_INPUT = 0

    @staticmethod
    def validate_input(n):
        if not isinstance(n, int):
            raise TypeError("Input must be an integer")
        if n < FactorialCalculator.MIN_INPUT:
            raise ValueError("Factorial is not defined for negative numbers")

    @staticmethod
    def calculate(n):
        FactorialCalculator.validate_input(n)
        result = 1
        if n > 1:
            for i in range(2, n + 1):
                result *= i
        return result

if __name__ == '__main__':
    print(FactorialCalculator.calculate(0))
    print(FactorialCalculator.calculate(1))
    print(FactorialCalculator.calculate(7))
    print(FactorialCalculator.calculate(12))
    try:
        FactorialCalculator.calculate(-3)
    except ValueError as e:
        print(str(e))
    try:
        FactorialCalculator.calculate(3.5)
    except TypeError as e:
        print(str(e))