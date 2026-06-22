def reverse_integer(n):
    is_negative = n < 0
    n = abs(n)
    reversed_str = str(n)[::-1]
    reversed_int = int(reversed_str)
    if is_negative:
        return -reversed_int
    return reversed_int

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(120))
    print(reverse_integer(0))
    print(reverse_integer(1))
    print(reverse_integer(-1))
    print(reverse_integer(1000))
    print(reverse_integer(-1000))