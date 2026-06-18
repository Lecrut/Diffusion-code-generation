def check_divisibility(dividend: int, divisor: int) -> bool:
    """Check if dividend is divisible by divisor (divisor cannot be zero)."""
    return divisor != 0 and dividend % divisor == 0

if __name__ == '__main__':
    sample_first = 15
    sample_second = 3

    result = check_divisibility(sample_first, sample_second)
    if result:
        print('True')
    else:
        print('False')