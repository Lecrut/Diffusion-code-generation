def reverse_integer(x):
    sign = -1 if x < 0 else 1
    x = abs(x)
    reversed_x = 0
    while x != 0:
        digit = x % 10
        x //= 10
        reversed_x = reversed_x * 10 + digit
    result = sign * reversed_x
    if result < -2**31 or result > 2**31 - 1:
        return 0
    return result

if __name__ == '__main__':
    sample_values = [123, -456, 120, 0, 1534236469, -2147483648]
    for val in sample_values:
        print(reverse_integer(val))