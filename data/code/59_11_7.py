def compute_digit_sum(number: int) -> int:
    total = 0
    if number < 0:
        number = -number
    while number > 0:
        total += number % 10
        number //= 10
    return total

if __name__ == '__main__':
    sample_values = [123456789012345678, 999999999999999999, 1000000000000000000, 0]
    for value in sample_values:
        result = compute_digit_sum(value)
        print(result)