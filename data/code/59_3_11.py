def sum_digits(number: int) -> int:
    return sum([int(digit) for digit in str(abs(number))])

if __name__ == '__main__':
    result = sum_digits(12345678901234567890)
    print(result)