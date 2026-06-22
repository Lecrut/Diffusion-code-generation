def sum_digits(number: int) -> int:
    absolute_number = abs(number)
    digit_sum = 0
    while absolute_number > 0:
        digit_sum += absolute_number % 10
        absolute_number //= 10
    return digit_sum

if __name__ == '__main__':
    large_integer = 123456789012345678901234567890
    result = sum_digits(large_integer)
    print(result)