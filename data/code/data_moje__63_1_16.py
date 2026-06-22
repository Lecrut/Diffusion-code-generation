def reverse_integer(n):
    if n == 0:
        return 0
    negative = n < 0
    if negative:
        n = -n
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    if reversed_num > 2**31 - 1:
        return 0
    return -reversed_num if negative else reversed_num

if __name__ == '__main__':
    test_values = [123, -456, 0, 1534236469, -2147483412]
    for val in test_values:
        print(reverse_integer(val))