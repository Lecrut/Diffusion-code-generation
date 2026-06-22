def reverse_integer(n):
    if n == 0:
        return 0
    negative = n < 0
    x = -n if negative else n
    result = 0
    while x > 0:
        digit = x % 10
        result = result * 10 + digit
        x //= 10
    if negative:
        result = -result
    if result > 2**31 - 1 or result < -2**31:
        return 0
    return result

if __name__ == '__main__':
    test_values = [123, -456, 1200, 0, 1534236469]
    for value in test_values:
        print(reverse_integer(value))