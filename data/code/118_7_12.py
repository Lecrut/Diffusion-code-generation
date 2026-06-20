def multiply(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a & b + (a ^ b) << 1
    else:
        return a * b
if __name__ == '__main__':
    print(multiply(5, 3))
    print(multiply(4.5, 2))