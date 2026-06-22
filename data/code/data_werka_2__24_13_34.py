def is_negative(value):
    return isinstance(value, (int, float)) and value < 0

if __name__ == '__main__':
    test_cases = [42, -17, 0.0, -2.718, 'world', None]
    outcomes = {case: is_negative(case) for case in test_cases}
    print(outcomes)