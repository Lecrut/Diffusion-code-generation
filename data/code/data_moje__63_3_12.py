def reverse_integer(n):
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_num = 0
    while n != 0:
        digit = n % 10
        n //= 10
        if reversed_num > (INT_MAX - digit) // 10:
            return 0
        reversed_num = reversed_num * 10 + digit
    return sign * reversed_num

if __name__ == '__main__':
    test_values = [123, -456, 1534236469, 0, -9876543212]
    for val in test_values:
        result = reverse_integer(val)
        print(f"{val} -> {result}")