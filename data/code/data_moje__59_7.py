def sum_digits(n):
    total = 0
    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10
    return total

if __name__ == '__main__':
    print(sum_digits(0))
    print(sum_digits(12345))
    print(sum_digits(999))
    print(sum_digits(100))