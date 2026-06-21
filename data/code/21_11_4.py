def find_largest(a, b, c):
    return a if a >= b and a >= c else (b if b >= a and b >= c else c)

if __name__ == '__main__':
    x = 10
    y = 25
    z = 15
    print(find_largest(x, y, z))