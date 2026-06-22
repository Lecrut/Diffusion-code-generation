def analyze_integers(a, b, c):
    checks = {
        'a_positive': a > 0,
        'b_even': b % 2 == 0,
        'c_divisible_by_a': False
    }
    if a != 0:
        checks['c_divisible_by_a'] = c % a == 0
    return tuple(checks.values())

if __name__ == '__main__':
    result = analyze_integers(3, 4, 12)
    print(result)