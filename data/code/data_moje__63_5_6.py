def reverse_integer(n):
    sign = -1 if n < 0 else 1
    n_abs = abs(n)
    reversed_n = 0
    while n_abs > 0:
        digit = n_abs % 10
        reversed_n = reversed_n * 10 + digit
        n_abs //= 10
    return sign * reversed_n

if __name__ == '__main__':
    samples = [123, -456, 120, 0, -7]
    for s in samples:
        print(reverse_integer(s))