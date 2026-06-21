def is_greater(num1, num2):
    return num1 > num2

if __name__ == '__main__':
    SAMPLE_VALUE_1 = 50
    SAMPLE_VALUE_2 = 30
    result = is_greater(SAMPLE_VALUE_1, SAMPLE_VALUE_2)
    print(result)

    TEST_CASES = [
        (10, 5),
        (3, 7),
        (-1, -5),
        (0, 0),
        (100, 100),
        (-10, -20)
    ]
    for num1, num2 in TEST_CASES:
        comparison_result = is_greater(num1, num2)
        print(f"is_greater({num1}, {num2}) = {comparison_result}")