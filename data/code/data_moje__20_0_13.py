def is_even(n: int) -> bool:
    remainder = n % 2
    return remainder == 0

if __name__ == '__main__':
    test_value_1 = 22
    test_value_2 = -15
    result_1 = is_even(test_value_1)
    result_2 = is_even(test_value_2)
    print(result_1)
    print(result_2)