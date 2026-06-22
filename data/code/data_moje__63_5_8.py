def reverse_integer(x):
    if x == 0:
        return 0
    sign = -1 if x < 0 else 1
    x = abs(x)
    reversed_num = 0
    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10
    result = sign * reversed_num
    if result < -2**31 or result > 2**31 - 1:
        return 0
    return result

if __name__ == '__main__':
    test_values = [123, -123, 120, 0, 1534236469]
    for val in test_values:
        print(reverse_integer(val))