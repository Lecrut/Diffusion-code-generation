def multiply_integers(a: object, b: object) -> int:
    a = int(a) if not isinstance(a, int) else a
    b = int(b) if not isinstance(b, int) else b
    return a * b
if __name__ == '__main__':
    print(multiply_integers(3.5, 4))