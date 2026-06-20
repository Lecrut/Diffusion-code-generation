def combine_checks(a, b, c):
    return a > 0 and b % 2 == 0 and c % a == 0

if __name__ == '__main__':
    print(combine_checks(5, 4, 10))