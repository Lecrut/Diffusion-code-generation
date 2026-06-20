def is_negative(number):
    return number < 0

if __name__ == '__main__':
    test_cases = [-5.0, 0, 3.14]
    for case in test_cases:
        print(is_negative(case))