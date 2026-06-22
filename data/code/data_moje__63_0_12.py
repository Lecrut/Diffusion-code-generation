def reverse_integer(n):
    sign = -1 if n < 0 else 1
    reversed_abs = 0
    n_abs = abs(n)
    while n_abs != 0:
        digit = n_abs % 10
        reversed_abs = reversed_abs * 10 + digit
        n_abs //= 10
    result = sign * reversed_abs
    if result < -2147483648 or result > 2147483647:
        return 0
    return result

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(1534236469))
    print(reverse_integer(0))
    print(reverse_integer(-2147483648))
    print(reverse_integer(2147483647))