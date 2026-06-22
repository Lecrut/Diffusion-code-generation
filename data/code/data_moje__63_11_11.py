def reverse_integer(n):
    if n < 0:
        reversed_str = str(n)[1:][::-1]
        reversed_int = int(reversed_str)
        return -reversed_int
    else:
        reversed_str = str(n)[::-1]
        reversed_int = int(reversed_str)
        return reversed_int

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(7890))
    print(reverse_integer(0))
    print(reverse_integer(-100))