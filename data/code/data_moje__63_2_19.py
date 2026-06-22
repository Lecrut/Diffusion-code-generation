def reverse_integer(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_n = 0
    while n > 0:
        reversed_n = reversed_n * 10 + n % 10
        n //= 10
    reversed_n *= sign
    INT_MIN = -(2 ** 31)
    INT_MAX = 2 ** 31 - 1
    if reversed_n < INT_MIN or reversed_n > INT_MAX:
        return 0
    return reversed_n

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(120))
    print(reverse_integer(1534236469))