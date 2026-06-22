def reverse_integer(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_n = 0
    while n > 0:
        digit = n % 10
        reversed_n = reversed_n * 10 + digit
        n //= 10
    result = sign * reversed_n
    INT32_MAX = 2**31 - 1
    INT32_MIN = -2**31
    if result < INT32_MIN or result > INT32_MAX:
        return 0
    return result

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(120))
    print(reverse_integer(0))
    print(reverse_integer(1534236469))
    print(reverse_integer(-2147483648))
    print(reverse_integer(2147483647))