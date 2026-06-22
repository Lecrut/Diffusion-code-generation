def reverse_integer(n):
    negative = n < 0
    abs_str = str(abs(n))
    reversed_str = abs_str[::-1]
    reversed_int = int(reversed_str)
    if negative:
        return -reversed_int
    return reversed_int

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(1200))
    print(reverse_integer(0))