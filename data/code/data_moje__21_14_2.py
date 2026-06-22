def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    return c

if __name__ == '__main__':
    x = 12.5
    y = 30.1
    z = 5.7
    result = find_largest(x, y, z)
    print(result)