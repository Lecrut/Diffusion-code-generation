def reverse_integer(x: int) -> int:
    sign = -1 if x < 0 else 1
    x_abs = abs(x)
    reversed_abs = 0
    while x_abs != 0:
        digit = x_abs % 10
        reversed_abs = reversed_abs * 10 + digit
        x_abs //= 10
    
    reversed_x = sign * reversed_abs
    if reversed_x < -2**31 or reversed_x > 2**31 - 1:
        return 0
    return reversed_x

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(1534236469))
    print(reverse_integer(0))
    print(reverse_integer(10))