def sum_digits(n: int) -> int:
    return sum(int(digit) for digit in str(abs(n)))

if __name__ == '__main__':
    large_integer = 987654321012345678901234567890
    result = sum_digits(large_integer)
    print(result)