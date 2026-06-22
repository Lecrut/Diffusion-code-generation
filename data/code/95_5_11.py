def analyze_integers(a, b, c):
    criteria = {
        'positive': lambda x: x > 0,
        'even': lambda x: x % 2 == 0,
        'divisible_by_first': lambda x: a != 0 and x % a == 0
    }
    
    check_positive = criteria['positive'](a)
    check_even = criteria['even'](b)
    check_divisible = criteria['divisible_by_first'](c)
    
    return (check_positive, check_even, check_divisible)

if __name__ == '__main__':
    sample_a = 15
    sample_b = 8
    sample_c = 30
    output = analyze_integers(sample_a, sample_b, sample_c)
    print(output)