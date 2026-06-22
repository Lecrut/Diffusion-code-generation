def is_float_pi(value):
    if not isinstance(value, float):
        return False
    return value == 3.14

if __name__ == '__main__':
    test_cases = [3.14, 3.14159, '3.14', 3, 3.1400000000000001]
    for case in test_cases:
        print(is_float_pi(case))