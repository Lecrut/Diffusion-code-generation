def sum_of_digits(number):
    return sum([int(digit) for digit in str(abs(number))])

if __name__ == '__main__':
    sample_number = 123456789012345678901234567890
    print(sum_of_digits(sample_number))
    print(sum_of_digits(-98765))