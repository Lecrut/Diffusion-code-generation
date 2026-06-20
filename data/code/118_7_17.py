def multiply(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a * b
    else:
        return a * b
if __name__ == '__main__':
    print(multiply(5, 3))
    print(multiply(-5, 3))
    print(multiply(0, 5))
    print(multiply(-10, 0))
    print(multiply(5.5, 2))