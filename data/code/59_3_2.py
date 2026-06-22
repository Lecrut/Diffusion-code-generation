def sum_of_digits(number: int) -> int:
    return sum(int(digit) for digit in str(abs(number)))

if __name__ == '__main__':
    sample_value = 123456789012345678901234567890
    result = sum_of_digits(sample_value)
    print(result)