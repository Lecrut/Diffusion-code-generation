def find_max(a, b, c):
    return a if a > b and a > c else (b if b > c else c)

if __name__ == '__main__':
    x = 10
    y = 25
    z = 5
    print(find_max(x, y, z))