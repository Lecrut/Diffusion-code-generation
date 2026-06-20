def is_negative(number):
    return number < 0
if __name__ == '__main__':
    TEST_CASES = [-5.0, 0, 3.14]
    for case in TEST_CASES:
        print(is_negative(case))