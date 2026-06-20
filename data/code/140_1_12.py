def is_even(number):
    return (number & 1) == 0

if __name__ == '__main__':
    test_cases = [4, 7, 23, 42]
    for case in test_cases:
        print(is_even(case))