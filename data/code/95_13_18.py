def validate_input(a, b, c):
    return all(x > 0 and x % 2 == 0 and x < 100 for x in (a, b, c))

if __name__ == '__main__':
    test_cases = [
        (10, 20, 30),
        (100, 20, 30),
        (5, 10, 12),
        (10, 21, 30),
        (10, 20, 101)
    ]
    for case in test_cases:
        print(validate_input(*case))