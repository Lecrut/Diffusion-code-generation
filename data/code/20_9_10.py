class NumberChecker:
    EVEN_MASK = 0b1

    @staticmethod
    def is_even(n: int) -> bool:
        return (n & NumberChecker.EVEN_MASK) == 0

if __name__ == '__main__':
    test_values = [18, 25, -12, 0, 31]
    for value in test_values:
        print(NumberChecker.is_even(value))