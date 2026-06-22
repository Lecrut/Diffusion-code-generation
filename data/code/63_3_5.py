def reverse_integer(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_n = 0
    while n > 0:
        digit = n % 10
        reversed_n = reversed_n * 10 + digit
        n //= 10
    reversed_n *= sign
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31
    if reversed_n < INT_MIN or reversed_n > INT_MAX:
        return 0
    return reversed_n

if __name__ == '__main__':
    sample_values = [123, -456, 120, 0, 1534236469, -2147483648]
    for val in sample_values:
        print(reverse_integer(val))