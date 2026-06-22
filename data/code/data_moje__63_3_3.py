INT_MAX = 2147483647
INT_MIN = -2147483648

def reverse_integer(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_num = 0
    while n > 0:
        digit = n % 10
        if reversed_num > INT_MAX // 10 or (reversed_num == INT_MAX // 10 and digit > 7):
            return 0
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return sign * reversed_num

if __name__ == '__main__':
    test_values = [123, -123, 1534236469, 0, -2147483648]
    for value in test_values:
        result = reverse_integer(value)
        print(result)