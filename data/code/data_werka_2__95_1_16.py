def combine_checks(first, second, third):
    conditions = {
        'positive': lambda x: x > 0,
        'even': lambda x: x % 2 == 0,
        'divisible': lambda x, y: x % y == 0
    }
    check_positive = conditions['positive'](first)
    check_even = conditions['even'](second)
    check_divisible = conditions['divisible'](third, first)
    return check_positive and check_even and check_divisible

if __name__ == '__main__':
    print(combine_checks(2, 4, 8))
    print(combine_checks(3, 4, 12))
    print(combine_checks(1, 2, 3))
    print(combine_checks(-1, 4, 2))
    print(combine_checks(5, 6, 10))