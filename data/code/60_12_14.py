class FactorialCalculator:
    ZERO_RESULT = 1
    MIN_VALID_INPUT = 0

    @staticmethod
    def validate_input(n):
        if isinstance(n, bool):
            raise TypeError("Input must be an integer")
        if not isinstance(n, int):
            raise TypeError("Input must be an integer")
        if n < FactorialCalculator.MIN_VALID_INPUT:
            raise ValueError("Input must be a non-negative integer")

    @staticmethod
    def compute(n):
        FactorialCalculator.validate_input(n)
        if n == 0:
            return FactorialCalculator.ZERO_RESULT
        result = 1
        current = 2
        while current <= n:
            result *= current
            current += 1
        return result

if __name__ == '__main__':
    print(FactorialCalculator.compute(5))
    print(FactorialCalculator.compute(0))
    print(FactorialCalculator.compute(1))
    print(FactorialCalculator.compute(7))