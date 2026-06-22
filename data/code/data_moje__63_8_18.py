def reverse_integer(x):
    INT_MAX = 2147483647
    INT_MIN = -2147483648
    sign = -1 if x < 0 else 1
    x = abs(x)
    reversed_x = 0
    while x != 0:
        digit = x % 10
        if reversed_x > (INT_MAX - digit) // 10:
            return 0
        reversed_x = reversed_x * 10 + digit
        x //= 10
    result = sign * reversed_x
    if result < INT_MIN or result > INT_MAX:
        return 0
    return result

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(1534236469))