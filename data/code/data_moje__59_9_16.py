def sum_digits(n: int) -> int:
    if n < 0:
        n = -n
    total: int = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

if __name__ == '__main__':
    number: int = 123456789012345678901234567890
    result: int = sum_digits(number)
    print(result)