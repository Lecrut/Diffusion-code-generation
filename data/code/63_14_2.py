def reverse_integer(n):
    if n < 0:
        return -int(str(-n)[::-1])
    return int(str(n)[::-1])

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(7890))
    print(reverse_integer(0))