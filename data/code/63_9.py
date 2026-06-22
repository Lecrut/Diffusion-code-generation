def reverse_integer(n):
    sign = -1 if n < 0 else 1
    abs_n = abs(n)
    reversed_digits = 0
    while abs_n > 0:
        digit = abs_n % 10
        reversed_digits = reversed_digits * 10 + digit
        abs_n //= 10
    return sign * reversed_digits

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(1200))
    print(reverse_integer(0))
    print(reverse_integer(7))
    print(reverse_integer(-101))