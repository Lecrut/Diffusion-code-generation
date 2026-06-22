def reverse_integer(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_str = str(n)[::-1]
    reversed_num = int(reversed_str)
    return sign * reversed_num

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(1200))
    print(reverse_integer(0))
    print(reverse_integer(-10))