def sum_of_digits(number):
    return sum([int(digit) for digit in str(number)])

if __name__ == '__main__':
    sample_value = 12345
    result = sum_of_digits(sample_value)
    print(result)
    sample_value_2 = 9876543210
    result_2 = sum_of_digits(sample_value_2)
    print(result_2)