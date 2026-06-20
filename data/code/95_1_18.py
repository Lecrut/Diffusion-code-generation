def combine_checks(a, b, c):
    if a <= 0:
        return False
    if b % 2 != 0:
        return False
    if c % a != 0:
        return False
    return True

if __name__ == '__main__':
    print(combine_checks(3, 4, 12))
    print(combine_checks(5, 6, 10))
    print(combine_checks(2, 8, 10))
    print(combine_checks(-1, 4, 2))
    print(combine_checks(1, 5, 10))