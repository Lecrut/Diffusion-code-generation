def reverse_integer(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_val = 0
    while n > 0:
        digit = n % 10
        reversed_val = reversed_val * 10 + digit
        n //= 10
    return sign * reversed_val

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(1200))
    print(reverse_integer(0))
    print(reverse_integer(-98100))