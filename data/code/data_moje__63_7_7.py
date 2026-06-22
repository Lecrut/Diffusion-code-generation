def reverse_integer(n):
    if n == 0:
        return 0
    sign = -1 if n < 0 else 1
    abs_n = abs(n)
    reversed_n = 0
    while abs_n > 0:
        reversed_n = reversed_n * 10 + abs_n % 10
        abs_n = abs_n // 10
    return sign * reversed_n

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(1200))