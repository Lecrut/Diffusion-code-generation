def reverse_integer(n):
    negative = n < 0
    abs_n = abs(n)
    reversed_str = str(abs_n)[::-1]
    reversed_int = int(reversed_str)
    if negative:
        reversed_int = -reversed_int
    return reversed_int

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(120))
    print(reverse_integer(0))
    print(reverse_integer(-100))