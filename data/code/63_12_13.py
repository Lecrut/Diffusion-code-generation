def reverse_integer(n):
    negative = n < 0
    digits = [c for c in str(abs(n)) if c.isdigit()]
    reversed_digits = digits[::-1]
    reversed_str = ''.join(reversed_digits)
    reversed_int = int(reversed_str)
    if negative:
        reversed_int = -reversed_int
    return reversed_int

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(1200))
    print(reverse_integer(0))
    print(reverse_integer(1000000003))