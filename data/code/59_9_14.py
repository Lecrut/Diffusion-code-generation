def sum_digits(n: int) -> int:
    return sum(int(digit) for digit in str(abs(n)))

if __name__ == '__main__':
    result = sum_digits(123456789012345678901234567890)
    print(result)