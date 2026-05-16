def combine_checks(a, b, c):
    return a > 0 and b % 2 == 0 and c % a == 0
if __name__ == '__main__':
    print(combine_checks(2, 4, 8))
    print(combine_checks(3, 6, 9))
    print(combine_checks(1, 2, 3))
    print(combine_checks(-1, 4, 8))
    print(combine_checks(5, 6, 10))