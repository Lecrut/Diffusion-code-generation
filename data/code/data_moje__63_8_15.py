def reverse_integer(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_num = 0
    while n:
        digit = n % 10
        n //= 10
        reversed_num = reversed_num * 10 + digit
        if reversed_num > 2**31 - 1:
            return 0
    return sign * reversed_num

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(120))
    print(reverse_integer(1534236469))
    print(reverse_integer(0))