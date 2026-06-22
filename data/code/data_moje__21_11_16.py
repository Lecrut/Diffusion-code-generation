def find_largest(a, b, c):
    return a if a > b and a > c else (b if b > c else c)

if __name__ == '__main__':
    x = 10
    y = 30
    z = 20
    result = find_largest(x, y, z)
    print(result)