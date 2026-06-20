def is_negative(number):
    NEGATIVE_THRESHOLD = 0
    return number < NEGATIVE_THRESHOLD

if __name__ == '__main__':
    test_cases = [-5.0, 0, 3.14]
    for case in test_cases:
        print(is_negative(case))