def reverse_integer(n):
    negative = n < 0
    s = str(abs(n))
    reversed_s = "".join([c for c in reversed(s)])
    result = int(reversed_s)
    if negative:
        result = -result
    return result

if __name__ == '__main__':
    print(reverse_integer(1234))
    print(reverse_integer(-456))
    print(reverse_integer(1200))
    print(reverse_integer(0))