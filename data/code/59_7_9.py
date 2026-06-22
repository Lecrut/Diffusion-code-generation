def sum_digits(n):
    if n < 0:
        return 0
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10
    return total

if __name__ == '__main__':
    print(sum_digits(123))
    print(sum_digits(0))
    print(sum_digits(999))