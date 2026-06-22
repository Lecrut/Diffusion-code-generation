import sys

def reverse_integer(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_num = 0
    while n > 0:
        digit = n % 10
        if reversed_num > (sys.maxsize - digit) // 10:
            return 0
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return sign * reversed_num

if __name__ == '__main__':
    test_values = [123, -123, 1534236469, 0, 1000]
    for val in test_values:
        print(reverse_integer(val))