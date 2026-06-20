def is_positive(num):
    return num > 0

def is_even(num):
    return num % 2 == 0

def is_divisible(dividend, divisor):
    return dividend % divisor == 0

def combine_checks(a, b, c):
    if not (is_positive(a) and is_even(b) and is_divisible(c, a)):
        return False
    return True

if __name__ == '__main__':
    print(combine_checks(3, 4, 12))
    print(combine_checks(5, 6, 10))
    print(combine_checks(2, 8, 10))
    print(combine_checks(-1, 4, 2))
    print(combine_checks(1, 5, 10))