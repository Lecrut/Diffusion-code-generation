def sum_digits(n):
    n = abs(n)
    if n == 0:
        return 0
    digits = []
    while n:
        digits.append(n % 10)
        n //= 10
    return sum(digits)

if __name__ == '__main__':
    print(sum_digits(12345))
    print(sum_digits(-67890))
    print(sum_digits(0))
    print(sum_digits(9999999999))