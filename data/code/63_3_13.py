INT_MAX = 2147483647
INT_MIN = -2147483648

def reverse_integer(x):
    sign = -1 if x < 0 else 1
    x *= sign
    reversed_val = 0
    while x != 0:
        digit = x % 10
        x //= 10
        if reversed_val > (INT_MAX // 10) or (reversed_val == INT_MAX // 10 and digit > 7):
            return 0
        if reversed_val < (INT_MIN // 10) or (reversed_val == INT_MIN // 10 and digit < -8):
            return 0
        reversed_val = reversed_val * 10 + digit
    return sign * reversed_val

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(1534236469))
    print(reverse_integer(0))
    print(reverse_integer(10))