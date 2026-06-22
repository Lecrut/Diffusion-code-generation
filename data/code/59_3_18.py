def sum_digits(number: int) -> int:
    return sum(int(digit) for digit in str(abs(number)))

if __name__ == '__main__':
    sample_value = 12345678901234567890
    result = sum_digits(sample_value)
    print(result)