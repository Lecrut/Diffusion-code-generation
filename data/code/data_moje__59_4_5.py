def sum_of_digits(number):
    abs_number = abs(number)
    total = 0
    while abs_number > 0:
        total += abs_number % 10
        abs_number //= 10
    return total

if __name__ == '__main__':
    test_value_1 = 12345
    test_value_2 = -9876
    result_1 = sum_of_digits(test_value_1)
    result_2 = sum_of_digits(test_value_2)
    print(result_1)
    print(result_2)