def reverse_integer(n):
    sign = -1 if n < 0 else 1
    abs_n = abs(n)
    reversed_num = 0
    while abs_n > 0:
        digit = abs_n % 10
        reversed_num = reversed_num * 10 + digit
        abs_n //= 10
    return sign * reversed_num

if __name__ == '__main__':
    print(reverse_integer(12345))
    print(reverse_integer(-6789))
    print(reverse_integer(100))
    print(reverse_integer(0))