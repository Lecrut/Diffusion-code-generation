IS_POSITIVE = 'positive'
IS_EVEN = 'even'
IS_DIVISIBLE = 'divisible'

def validate_integers(a, b, c):
    checks = {
        IS_POSITIVE: a > 0,
        IS_EVEN: b % 2 == 0,
        IS_DIVISIBLE: c % a == 0
    }
    return tuple(checks.values())

if __name__ == '__main__':
    result = validate_integers(8, 15, 40)
    print(result)