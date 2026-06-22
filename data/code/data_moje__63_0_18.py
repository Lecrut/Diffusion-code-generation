def reverse_integer(n):
    rev = 0
    negative = n < 0
    n = abs(n)
    while n != 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
        if rev > 2**31 - 1:
            return 0
    return -rev if negative else rev

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(120))
    print(reverse_integer(0))
    print(reverse_integer(1534236469))