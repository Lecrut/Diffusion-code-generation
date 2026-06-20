def validate_integers(a, b, c):
    checks = {
        'positive': a > 0,
        'even': b % 2 == 0,
        'divisible': c % a == 0
    }
    return tuple(checks.values())

if __name__ == '__main__':
    result = validate_integers(7, 14, 28)
    print(result)