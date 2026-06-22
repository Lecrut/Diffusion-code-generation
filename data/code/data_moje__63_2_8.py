def reverse_integer(x):
    INT_MIN = -2147483648
    INT_MAX = 2147483647
    sign = -1 if x < 0 else 1
    x = abs(x)
    reversed_num = 0
    while x != 0:
        digit = x % 10
        x //= 10
        if reversed_num > INT_MAX // 10 or (reversed_num == INT_MAX // 10 and digit > 7):
            return 0
        reversed_num = reversed_num * 10 + digit
    result = sign * reversed_num
    if result < INT_MIN or result > INT_MAX:
        return 0
    return result

if __name__ == '__main__':
    test_values = [123, -123, 1534236469, 0, -2147483648, 2147483647]
    for val in test_values:
        print(reverse_integer(val))