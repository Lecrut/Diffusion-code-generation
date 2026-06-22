def compute_digit_sum(number: int) -> int:
    if number < 0:
        number = -number
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

if __name__ == '__main__':
    sample_large_number = 987654321012345678
    result = compute_digit_sum(sample_large_number)
    print(result)
    
    negative_sample = -123456789012345678
    negative_result = compute_digit_sum(negative_sample)
    print(negative_result)
    
    zero_sample = 0
    zero_result = compute_digit_sum(zero_sample)
    print(zero_result)