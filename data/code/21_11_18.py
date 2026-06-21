def get_largest(x, y, z):
    values = [x, y, z]
    for val in values:
        if not isinstance(val, (int, float)):
            raise TypeError("All inputs must be numeric")
    if x >= y and x >= z:
        return x
    if y >= z:
        return y
    return z

if __name__ == '__main__':
    a = 5
    b = 20
    c = 8
    print(get_largest(a, b, c))