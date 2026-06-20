class IntegerChecker:
    @staticmethod
    def is_positive(num):
        return num > 0

    @staticmethod
    def is_even(num):
        return num % 2 == 0

    @staticmethod
    def is_divisible(dividend, divisor):
        return dividend % divisor == 0

def check_integers(a, b, c):
    pos_a = IntegerChecker.is_positive(a)
    even_b = IntegerChecker.is_even(b)
    divisible_c_by_a = IntegerChecker.is_divisible(c, a)
    return (pos_a, even_b, divisible_c_by_a)

if __name__ == '__main__':
    result = check_integers(10, 12, 30)
    print(result)