def reverse_integer(n):
    if n < 0:
        reversed_str = "-" + str(n)[1:][::-1]
    else:
        reversed_str = str(n)[::-1]
    return int(reversed_str)

if __name__ == '__main__':
    print(reverse_integer(12345))
    print(reverse_integer(-6789))
    print(reverse_integer(1200))