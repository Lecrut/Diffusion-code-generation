def is_positive(value):
    return value > 0
if __name__ == '__main__':
    test_cases = [1, -5, 0, 3.14]
    for case in test_cases:
        print(f"{case}: {is_positive(case)}")