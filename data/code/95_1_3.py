def combine_checks(a, b, c):
    if a > 0 and b % 2 == 0 and c % a == 0:
        return True
    else:
        return False
if __name__ == '__main__':
    print(combine_checks(3, 4, 12))
    print(combine_checks(2, 6, 10))
    print(combine_checks(-1, 4, 8))
    print(combine_checks(5, 6, 11))