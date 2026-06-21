def get_max(x, y, z):
    if x >= y and x >= z:
        return x
    if y >= z:
        return y
    return z

if __name__ == '__main__':
    a = 100
    b = 50
    c = 200
    print(get_max(a, b, c))