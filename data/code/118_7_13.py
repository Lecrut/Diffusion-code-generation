def multiply(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a * b
    else:
        return a * b

if __name__ == '__main__':
    print(multiply(5, 3))
    print(multiply(2.5, 4))