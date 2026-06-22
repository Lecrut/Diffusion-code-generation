def reverse_integer(n):
    if n < 0:
        return -reverse_integer(-n)
    reversed_str = str(n)[::-1]
    return int(reversed_str)

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(120))
    print(reverse_integer(0))
    print(reverse_integer(-500))
    print(reverse_integer(7))