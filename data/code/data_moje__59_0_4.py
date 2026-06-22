def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

if __name__ == '__main__':
    test_value = 12345
    result = sum_of_digits(test_value)
    print(result)
    test_value_2 = 999999
    result_2 = sum_of_digits(test_value_2)
    print(result_2)