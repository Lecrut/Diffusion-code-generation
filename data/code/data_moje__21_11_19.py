def get_largest(a, b, c):
    return a if a > b and a > c else (b if b > c else c)

if __name__ == '__main__':
    x = 10
    y = 20
    z = 15
    print(get_largest(x, y, z))