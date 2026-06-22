def sum_digits(n: int) -> int:
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

if __name__ == '__main__':
    large_integer = 12345678901234567890
    result = sum_digits(large_integer)
    print(result)