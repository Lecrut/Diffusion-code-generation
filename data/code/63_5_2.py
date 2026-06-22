def reverse_integer(n):
    if n < 0:
        sign = -1
        n = -n
    else:
        sign = 1

    reversed_n = 0
    while n != 0:
        digit = n % 10
        reversed_n = reversed_n * 10 + digit
        n //= 10

    return sign * reversed_n

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(120))
    print(reverse_integer(0))