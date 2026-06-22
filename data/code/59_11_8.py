def compute_digit_sum(n: int) -> int:
    if n < 0:
        n = -n
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

if __name__ == '__main__':
    sample_large_number = 123456789012345678
    result = compute_digit_sum(sample_large_number)
    print(result)