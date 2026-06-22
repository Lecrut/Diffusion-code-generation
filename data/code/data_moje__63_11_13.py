def reverse_integer(n):
    is_negative = n < 0
    if is_negative:
        n = -n
    reversed_str = str(n)[::-1]
    reversed_int = int(reversed_str)
    if is_negative:
        reversed_int = -reversed_int
    return reversed_int

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(1200))
    print(reverse_integer(0))