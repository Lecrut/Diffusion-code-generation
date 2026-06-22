def reverse_integer(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    reversed_num *= sign
    if reversed_num < -2147483648 or reversed_num > 2147483647:
        return 0
    return reversed_num

if __name__ == '__main__':
    test_values = [123, -456, 1534236469, 0, -100, 2147483647, -2147483648, 1534236469, 1000]
    for val in test_values:
        print(val, reverse_integer(val))