def reverse_integer(n):
    sign = 1
    if n < 0:
        sign = -1
        n = -n
    reversed_str = str(n)[::-1]
    return sign * int(reversed_str)

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(0))
    print(reverse_integer(100))
    print(reverse_integer(-10))