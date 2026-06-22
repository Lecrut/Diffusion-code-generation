def sum_digits(n: int) -> int:
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

if __name__ == '__main__':
    test_values = [12345, -987654321, 0, 42]
    for value in test_values:
        print(sum_digits(value))