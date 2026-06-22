def sum_of_digits(n):
    if n < 10:
        return n
    return (n % 10) + sum_of_digits(n // 10)

if __name__ == '__main__':
    test_value_1 = 12345
    test_value_2 = 0
    test_value_3 = 9999
    result_1 = sum_of_digits(test_value_1)
    result_2 = sum_of_digits(test_value_2)
    result_3 = sum_of_digits(test_value_3)
    print(result_1)
    print(result_2)
    print(result_3)