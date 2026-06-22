def reverse_integer(n):
    if n < 0:
        return -int(str(n)[:0:-1])
    return int(str(n)[::-1])

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(1200))
    print(reverse_integer(0))
    print(reverse_integer(1000000003))