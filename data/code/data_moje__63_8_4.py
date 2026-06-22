def reverse_integer(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_n = 0
    while n != 0:
        digit = n % 10
        reversed_n = reversed_n * 10 + digit
        n //= 10
        if reversed_n > 2**31 - 1:
            return 0
    return sign * reversed_n

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(120))
    print(reverse_integer(1534236469))