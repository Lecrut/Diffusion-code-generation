def reverse_integer(n):
    sign = -1 if n < 0 else 1
    abs_n = abs(n)
    reversed_str = str(abs_n)[::-1]
    reversed_int = int(reversed_str)
    return sign * reversed_int

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(1200))
    print(reverse_integer(0))
    print(reverse_integer(1000000003))