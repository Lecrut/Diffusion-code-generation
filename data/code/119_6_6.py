def reverse_numbers(a, b):
    if a == 0:
        return (b, 0)
    q = b // a
    r = b - q * a
    x, y = a, r
    while r != 0:
        q = x // r
        t = r
        r = x - q * r
        x = t
    return (x, y)

if __name__ == '__main__':
    print(reverse_numbers(10, 20))