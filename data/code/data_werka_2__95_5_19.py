def analyze_integers(a, b, c):
    checks = {
        'first_positive': a > 0,
        'second_even': b % 2 == 0,
        'third_divisible': c % a == 0 if a != 0 else False
    }
    return (checks['first_positive'], checks['second_even'], checks['third_divisible'])

if __name__ == '__main__':
    result = analyze_integers(7, 8, 21)
    print(result)