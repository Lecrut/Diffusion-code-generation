def sum_digits(n: int) -> int:
    if n == 0:
        return 0
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

if __name__ == '__main__':
    print(sum_digits(0))
    print(sum_digits(123))
    print(sum_digits(987654321))
    print(sum_digits(1000000000))