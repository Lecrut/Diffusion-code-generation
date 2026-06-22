def compute_digit_sum(n: int) -> int:
    if n < 0:
        n = -n
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

if __name__ == '__main__':
    sample_numbers = [123456789012345678, 999999999999999999, 1000000000000000000]
    for num in sample_numbers:
        result = compute_digit_sum(num)
        print(f"Digit sum of {num}: {result}")