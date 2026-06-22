def is_greater(num1, num2):
    return num1 > num2

if __name__ == '__main__':
    SAMPLE_VALUE_1 = 42
    SAMPLE_VALUE_2 = 17
    RESULT = is_greater(SAMPLE_VALUE_1, SAMPLE_VALUE_2)
    print(RESULT)

    ADDITIONAL_TEST_CASES = [
        (50, 25),
        (8, 8),
        (-3, -6),
        (0.5, 0.2)
    ]
    for num1, num2 in ADDITIONAL_TEST_CASES:
        result = is_greater(num1, num2)
        print(f"is_greater({num1}, {num2}) = {result}")