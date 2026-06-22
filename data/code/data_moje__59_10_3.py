def sum_of_digits(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0:
        return 0
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

if __name__ == '__main__':
    print(sum_of_digits(0))
    print(sum_of_digits(5))
    print(sum_of_digits(123))
    print(sum_of_digits(9999))
    print(sum_of_digits(123456789))