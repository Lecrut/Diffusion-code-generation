def reverse_integer(x):
    sign = -1 if x < 0 else 1
    x_abs = abs(x)
    reversed_val = 0
    while x_abs != 0:
        digit = x_abs % 10
        reversed_val = reversed_val * 10 + digit
        x_abs //= 10
    result = sign * reversed_val
    if result < -2**31 or result > 2**31 - 1:
        return 0
    return result

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(120))
    print(reverse_integer(0))
    print(reverse_integer(1534236469))
    print(reverse_integer(1463847412))
    print(reverse_integer(-2147483648))
    print(reverse_integer(2147483647))