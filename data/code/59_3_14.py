def sum_digits(n):
    digits = [int(digit) for digit in str(abs(n))]
    return sum(digits)

if __name__ == '__main__':
    sample_number = 123456789
    result = sum_digits(sample_number)
    print(result)