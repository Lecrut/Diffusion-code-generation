class NumberChecker:
    DIVISOR_THREE = 3
    PARITY_EVEN = 0
    MIN_POSITIVE = 0

    @staticmethod
    def is_even(n):
        return n % NumberChecker.PARITY_EVEN == 0

    @staticmethod
    def is_divisible_by_three(n):
        return n % NumberChecker.DIVISOR_THREE == 0

    @staticmethod
    def is_positive(n):
        return n > NumberChecker.MIN_POSITIVE

    def check_all(self, n):
        return (
            NumberChecker.is_positive(n),
            NumberChecker.is_even(n),
            NumberChecker.is_divisible_by_three(n)
        )

if __name__ == '__main__':
    checker = NumberChecker()
    results = [checker.check_all(val) for val in [12, 18, 7, -3, 0]]
    for val, res in [(12, results[0]), (18, results[1]), (7, results[2]), (-3, results[3]), (0, results[4])]:
        print(f"{val} -> {res}")