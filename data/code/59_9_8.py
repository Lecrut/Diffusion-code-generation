def sum_digits(number: int) -> int:
    return sum(int(digit) for digit in str(abs(number)))

if __name__ == '__main__':
    large_integer: int = 123456789012345678901234567890
    result: int = sum_digits(large_integer)
    print(result)