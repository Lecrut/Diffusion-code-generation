def sum_digits(n: int) -> int:
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

if __name__ == '__main__':
    print(sum_digits(0))
    print(sum_digits(5))
    print(sum_digits(123))
    print(sum_digits(9876543210))
    print(sum_digits(11111111111111111111))