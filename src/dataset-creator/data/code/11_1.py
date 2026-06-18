def basic_arithmetic(a, b, c):
    return a * b + b * c + c * a
if __name__ == '__main__':
    x = 2
    y = 3
    z = 4
    result = basic_arithmetic(x, y, z)
    print(result)