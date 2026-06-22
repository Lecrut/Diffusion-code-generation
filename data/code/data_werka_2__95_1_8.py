def combine_checks(a, b, c):
    conditions = {
        'positive': lambda x: x > 0,
        'even': lambda x: x % 2 == 0,
        'divisible': lambda x, y: x % y == 0
    }
    
    check_positive = conditions['positive'](a)
    check_even = conditions['even'](b)
    check_divisible = conditions['divisible'](c, a)
    
    return check_positive and check_even and check_divisible

if __name__ == '__main__':
    result1 = combine_checks(4, 6, 12)
    print(result1)
    
    result2 = combine_checks(3, 5, 9)
    print(result2)
    
    result3 = combine_checks(-2, 4, 8)
    print(result3)
    
    result4 = combine_checks(5, 10, 25)
    print(result4)
    
    result5 = combine_checks(2, 3, 6)
    print(result5)