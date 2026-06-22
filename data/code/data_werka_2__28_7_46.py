def is_larger(a, b):
    comparison_operators = {
        'greater': lambda x, y: x > y,
        'less': lambda x, y: x < y,
        'equal': lambda x, y: x == y
    }
    return comparison_operators['greater'](a, b)

if __name__ == '__main__':
    test_cases = [
        (10, 5),
        (3, 7),
        (-1, -2),
        (0, 0),
        (5.5, 4.5),
        (2, 2)
    ]
    
    for a, b in test_cases:
        print(is_larger(a, b))