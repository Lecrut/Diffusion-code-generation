def is_negative(num):
    return num < 0

if __name__ == '__main__':
    test_cases = [-5, 3, 0, -1.5]
    for case in test_cases:
        print(is_negative(case))