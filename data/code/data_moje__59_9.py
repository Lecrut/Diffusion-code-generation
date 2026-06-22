def sum_digits(number: int) -> int:
    return sum(int(digit) for digit in str(number))

if __name__ == '__main__':
    large_number = 12345678901234567890
    result = sum_digits(large_number)
    print(result)