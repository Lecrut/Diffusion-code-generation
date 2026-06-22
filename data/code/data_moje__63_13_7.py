def reverse_integer(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    return sign * reversed_num

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(120))
    print(reverse_integer(0))
    print(reverse_integer(7))
    print(reverse_integer(100003))