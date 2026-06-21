def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

if __name__ == '__main__':
    x = 10
    y = 45
    z = 23
    result = find_largest(x, y, z)
    print(result)