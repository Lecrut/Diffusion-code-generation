def reverse_integer(n):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    reversed_n = 0
    sign = -1 if n < 0 else 1
    n = abs(n)
    while n != 0:
        digit = n % 10
        reversed_n = reversed_n * 10 + digit
        n //= 10
        if sign * reversed_n > INT_MAX or sign * reversed_n < INT_MIN:
            return 0
    return sign * reversed_n

if __name__ == '__main__':
    sample_values = [123, -123, 120, 0, 1534236469, -2147483412, 2147483648]
    for val in sample_values:
        print(reverse_integer(val))