def combine_checks(first, second, third):
    checks = {
        'positive': lambda x: x > 0,
        'even': lambda x: x % 2 == 0,
        'divisible': lambda x, y: x % y == 0
    }
    cond1 = checks['positive'](first)
    cond2 = checks['even'](second)
    cond3 = checks['divisible'](third, first)
    return cond1 and cond2 and cond3

if __name__ == '__main__':
    print(combine_checks(4, 6, 12))
    print(combine_checks(3, 5, 9))
    print(combine_checks(-2, 4, 8))
    print(combine_checks(2, 3, 6))
    print(combine_checks(5, 10, 20))