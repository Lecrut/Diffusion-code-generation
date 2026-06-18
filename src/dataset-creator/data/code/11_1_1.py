def basic_arithmetic(a, b, c):
    return a * b + b * c + c * a
if __name__ == '__main__':
    x = 1
    y = 2
    z = 3
    result = basic_arithmetic(x, y, z)
    print(result)