def reverse_integer(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_n = 0
    while n:
        digit = n % 10
        reversed_n = reversed_n * 10 + digit
        n //= 10
    reversed_n *= sign
    if reversed_n < -2**31 or reversed_n > 2**31 - 1:
        return 0
    return reversed_n

if __name__ == '__main__':
    sample_values = [123, -456, 1534236469, 0, -2147483648]
    for val in sample_values:
        print(reverse_integer(val))