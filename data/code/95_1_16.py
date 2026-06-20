def combine_checks(a, b, c):
    MIN_POSITIVE = 1
    EVEN_MODULO = 2
    DIVISIBILITY_MODULO = 0

    return a > MIN_POSITIVE and b % EVEN_MODULO == 0 and c % a == DIVISIBILITY_MODULO

if __name__ == '__main__':
    print(combine_checks(3, 4, 12))
    print(combine_checks(5, 6, 10))
    print(combine_checks(2, 8, 10))
    print(combine_checks(-1, 4, 2))
    print(combine_checks(1, 5, 10))