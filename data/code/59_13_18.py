def sum_of_digits(number):
    return sum([int(digit) for digit in str(number)])

if __name__ == '__main__':
    sample_value_1 = 12345
    sample_value_2 = 987654321
    result_1 = sum_of_digits(sample_value_1)
    result_2 = sum_of_digits(sample_value_2)
    print(result_1)
    print(result_2)