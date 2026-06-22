def sum_digits(value: int) -> int:
    negative = value < 0
    string_value = str(value) if not negative else str(value)[1:]
    total = 0
    for char in string_value:
        digit = int(char)
        total = total + digit
    return total

if __name__ == '__main__':
    number: int = 123456789012345678901234567890
    result: int = sum_digits(number)
    print(result)