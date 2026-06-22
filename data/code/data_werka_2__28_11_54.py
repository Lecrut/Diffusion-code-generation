def is_larger(num1, num2):
    return num1 > num2

if __name__ == '__main__':
    TEST_CASES = [
        (10, 5),
        (3, 7),
        (-1, -2),
        (0, 0),
        (5.5, 2),
        (-5, -6),
        (100, 99.9)
    ]

    for num1, num2 in TEST_CASES:
        print(is_larger(num1, num2))