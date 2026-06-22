def compute_digit_sum(number: int) -> int:
    if number < 0:
        number = -number
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

if __name__ == '__main__':
    test_value = 123456789012345678
    print(compute_digit_sum(test_value))
    print(compute_digit_sum(999999999999999999))
    print(compute_digit_sum(0))