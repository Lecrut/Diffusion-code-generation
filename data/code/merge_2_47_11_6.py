def multiply_integers(a: int, b: int) -> int:
    if not isinstance(a, int):
        raise TypeError(f"Expected 'int', got {type(a).__name__}")
    if not isinstance(b, int):
        raise TypeError(f"Expected 'int', got {type(b).__name__}")
    return a * b
if __name__ == '__main__':
    result = multiply_integers(10, 25)
    print(result)