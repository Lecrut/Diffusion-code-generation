def combine_checks(a, b, c):
    return a > 0 and b % 2 == 0 and (c % a == 0)
if __name__ == '__main__':
    print(combine_checks(3, 4, 6))
    print(combine_checks(-1, 2, 5))
    print(combine_checks(7, 8, 28))