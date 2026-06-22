def reverse_integer(x):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    sign = -1 if x < 0 else 1
    x = abs(x)
    reversed_x = 0
    while x:
        digit = x % 10
        x //= 10
        reversed_x = reversed_x * 10 + digit
    reversed_x *= sign
    if reversed_x < INT_MIN or reversed_x > INT_MAX:
        return 0
    return reversed_x

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(120))
    print(reverse_integer(0))
    print(reverse_integer(1534236469))