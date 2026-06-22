def sum_digits(n: int) -> int:
    total = 0
    n = abs(n)
    while n > 0:
        total += n % 10
        n //= 10
    return total

if __name__ == '__main__':
    large_integer = 123456789012345678901234567890
    result = sum_digits(large_integer)
    print(result)