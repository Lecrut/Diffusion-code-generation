def combine_checks(a, b, c):
    positive_check = a > 0
    even_check = b % 2 == 0
    divisibility_check = c % a == 0
    return positive_check and even_check and divisibility_check
if __name__ == '__main__':
    sample1 = combine_checks(3, 6, 9)
    sample2 = combine_checks(4, 8, 16)
    sample3 = combine_checks(-2, 4, -8)
    sample4 = combine_checks(5, 7, 35)
    sample5 = combine_checks(1, 0, 0)
    print(sample1)
    print(sample2)
    print(sample3)
    print(sample4)
    print(sample5)