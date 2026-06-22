def find_maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

if __name__ == '__main__':
    x = 10
    y = 25
    z = 15
    print(find_maximum(x, y, z))