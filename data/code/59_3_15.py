def sum_digits(number: int) -> int:
    absolute_value = abs(number)
    return sum(int(digit) for digit in str(absolute_value))

if __name__ == '__main__':
    large_positive = 123456789012345678901234567890
    large_negative = -987654321098765432109876543210
    print(sum_digits(large_positive))
    print(sum_digits(large_negative))
    print(sum_digits(0))
    print(sum_digits(12345))