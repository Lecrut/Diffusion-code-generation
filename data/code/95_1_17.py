def combine_checks(a, b, c):
    is_positive = a > 0
    is_even = b % 2 == 0
    is_divisible = c % a == 0
    return is_positive and is_even and is_divisible

if __name__ == '__main__':
    print(combine_checks(4, 6, 12))
    print(combine_checks(5, 8, 20))
    print(combine_checks(3, 10, 9))
    print(combine_checks(-1, 4, 8))
    print(combine_checks(2, 7, 14))