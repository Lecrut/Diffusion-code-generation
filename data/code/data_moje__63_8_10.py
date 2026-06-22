def reverse_integer(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_num = 0
    while n != 0:
        digit = n % 10
        n = n // 10
        if reversed_num > (2**31 - 1) // 10 or (reversed_num == (2**31 - 1) // 10 and digit > 7):
            return 0
        if sign == -1 and (reversed_num > 2**31 // 10 or (reversed_num == 2**31 // 10 and digit > 8)):
            return 0
        reversed_num = reversed_num * 10 + digit
    return sign * reversed_num

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(120))
    print(reverse_integer(1534236469))
    print(reverse_integer(0))
    print(reverse_integer(-2147483648))