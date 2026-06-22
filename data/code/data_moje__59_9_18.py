def sum_digits_of_large_integer(number: int) -> int:
    return sum(int(digit) for digit in str(abs(number)))

if __name__ == '__main__':
    large_number: int = 123456789012345678901234567890
    result: int = sum_digits_of_large_integer(large_number)
    print(result)