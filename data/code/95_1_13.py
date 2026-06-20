def combine_checks(a, b, c):
    return a > 0 and b % 2 == 0 and c % a == 0

if __name__ == '__main__':
    test_cases = [
        (3, 4, 12),
        (5, 6, 10),
        (2, 8, 10),
        (-1, 4, 2),
        (1, 5, 10)
    ]
    
    for a, b, c in test_cases:
        print(combine_checks(a, b, c))