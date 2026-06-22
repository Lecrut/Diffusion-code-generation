def sum_digits(number: int) -> int:
    total = 0
    n = abs(number)
    while n > 0:
        total += n % 10
        n //= 10
    return total

if __name__ == '__main__':
    large_integer = 9876543210123456789
    result = sum_digits(large_integer)
    print(result)