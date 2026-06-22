def sum_of_digits(n: int) -> int:
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

if __name__ == '__main__':
    test_value = 12345
    print(sum_of_digits(test_value))
    print(sum_of_digits(0))
    print(sum_of_digits(999999))