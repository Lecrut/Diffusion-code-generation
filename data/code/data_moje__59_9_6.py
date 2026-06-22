def sum_of_digits(number: int) -> int:
    total = 0
    for digit in str(abs(number)):
        total += int(digit)
    return total

if __name__ == '__main__':
    large_integer = 123456789012345678901234567890
    result = sum_of_digits(large_integer)
    print(result)