def sum_digits(number):
    abs_number = abs(number)
    total = 0
    for char in str(abs_number):
        total += int(char)
    return total

if __name__ == '__main__':
    sample_positive = 12345
    sample_negative = -9876
    result_positive = sum_digits(sample_positive)
    result_negative = sum_digits(sample_negative)
    print(result_positive)
    print(result_negative)