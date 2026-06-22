def reverse_integer(n):
    if n < 0:
        sign = -1
        n = -n
    else:
        sign = 1

    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10

    return sign * reversed_num

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(120))
    print(reverse_integer(0))
    print(reverse_integer(-100))
    print(reverse_integer(1))
    print(reverse_integer(-1))
    print(reverse_integer(10000))
    print(reverse_integer(-9090))