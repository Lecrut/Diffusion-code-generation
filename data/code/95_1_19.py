class CheckCombiner:
    @staticmethod
    def is_positive(number):
        return number > 0

    @staticmethod
    def is_even(number):
        return number % 2 == 0

    @staticmethod
    def is_divisible(dividend, divisor):
        return dividend % divisor == 0

    @classmethod
    def combine_checks(cls, a, b, c):
        return cls.is_positive(a) and cls.is_even(b) and cls.is_divisible(c, a)

if __name__ == '__main__':
    print(CheckCombiner.combine_checks(3, 4, 12))
    print(CheckCombiner.combine_checks(5, 6, 10))
    print(CheckCombiner.combine_checks(2, 8, 10))
    print(CheckCombiner.combine_checks(-1, 4, 2))
    print(CheckCombiner.combine_checks(1, 5, 10))