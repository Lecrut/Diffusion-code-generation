def reverse_integer(n):
    sign = -1 if n < 0 else 1
    reversed_str = ''.join(reversed(str(abs(n))))
    return sign * int(reversed_str)

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(1200))
    print(reverse_integer(0))