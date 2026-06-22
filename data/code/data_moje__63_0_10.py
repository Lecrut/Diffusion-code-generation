def reverse_integer(x):
    negative = x < 0
    abs_x = -x if negative else x
    result = 0
    while abs_x > 0:
        digit = abs_x % 10
        result = result * 10 + digit
        abs_x //= 10
    if negative:
        result = -result
    if result < -2147483648 or result > 2147483647:
        return 0
    return result

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(1534236469))
    print(reverse_integer(-2147483648))
    print(reverse_integer(0))