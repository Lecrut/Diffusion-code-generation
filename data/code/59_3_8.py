def sum_of_digits(number: int) -> int:
    number = abs(number)
    digits = [int(digit) for digit in str(number)]
    return sum(digits)

if __name__ == '__main__':
    test_value_1 = 12345
    test_value_2 = 9876543210
    test_value_3 = -500
    result_1 = sum_of_digits(test_value_1)
    result_2 = sum_of_digits(test_value_2)
    result_3 = sum_of_digits(test_value_3)
    print(result_1)
    print(result_2)
    print(result_3)