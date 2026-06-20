def multiply(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return (a << 0) + (b << 0)
    else:
        return a * b
if __name__ == '__main__':
    print(multiply(5, 3))
    print(multiply(-5, 3))
    print(multiply(0, 5))
    print(multiply(-10, 0))
    print(multiply(5, -3))
    print(multiply(100, 200))
    print(multiply(-1000, 500))