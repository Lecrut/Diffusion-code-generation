def reverse_integer(x):
    sign = -1 if x < 0 else 1
    x_abs = abs(x)
    reversed_num = 0
    while x_abs != 0:
        digit = x_abs % 10
        reversed_num = reversed_num * 10 + digit
        x_abs //= 10
    if reversed_num > 2**31 - 1:
        return 0
    return sign * reversed_num

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(1534236469))
    print(reverse_integer(0))
    print(reverse_integer(120))