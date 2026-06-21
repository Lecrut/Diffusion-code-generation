def get_greatest(a, b, c):
    return a if a >= b and a >= c else (b if b >= c else c)

if __name__ == '__main__':
    x = 10
    y = 25
    z = 15
    result = get_greatest(x, y, z)
    print(result)