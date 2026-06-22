def get_largest(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    return c

if __name__ == '__main__':
    x = 10.5
    y = 25.3
    z = 15.8
    print(get_largest(x, y, z))