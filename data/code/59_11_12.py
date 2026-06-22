def compute_digit_sum(number):
    if number == 0:
        return 0
    if number < 0:
        number = -number
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

if __name__ == '__main__':
    sample_large_number = 123456789012345678
    result = compute_digit_sum(sample_large_number)
    print(result)
    sample_negative = -999999999999999999
    result_neg = compute_digit_sum(sample_negative)
    print(result_neg)
    sample_zero = 0
    result_zero = compute_digit_sum(sample_zero)
    print(result_zero)