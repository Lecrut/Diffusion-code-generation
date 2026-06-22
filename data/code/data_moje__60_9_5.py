class FactorialComputer:
    MAX_DIGITS_THRESHOLD = 1000
    INITIAL_VALUE = 1

    @staticmethod
    def _validate_input(n):
        if not isinstance(n, int):
            raise TypeError("n must be an integer")
        if n < 0:
            raise ValueError("n must be non-negative")
        return n

    @staticmethod
    def _compute_iterative(n):
        if n == 0 or n == 1:
            return FactorialComputer.INITIAL_VALUE
        
        result = FactorialComputer.INITIAL_VALUE
        current = 2
        while current <= n:
            result *= current
            current += 1
        return result

    @staticmethod
    def get_factorial(n):
        FactorialComputer._validate_input(n)
        return FactorialComputer._compute_iterative(n)

if __name__ == '__main__':
    test_cases = [0, 1, 5, 10, 12]
    for case in test_cases:
        val = FactorialComputer.get_factorial(case)
        print(val)