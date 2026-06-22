def is_even(n):
    return n % 2 == 0

if __name__ == '__main__':
    test_cases = [0, 1, 2, 3, 4, -1, -2, 100, 99]
    for case in test_cases:
        print(is_even(case))