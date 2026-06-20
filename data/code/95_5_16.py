def check_integers(a, b, c):
    checks = {
        'positive': a > 0,
        'even': b % 2 == 0,
        'divisible': c % a == 0
    }
    return tuple(checks.values())

if __name__ == '__main__':
    result = check_integers(8, 16, 40)
    print(result)