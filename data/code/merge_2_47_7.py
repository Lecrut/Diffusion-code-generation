def multiply_integers(a: int, b: int) -> int:
    if not isinstance(a, int):
        raise TypeError(f"First argument must be an integer, got {type(a).__name__}")
    if not isinstance(b, int):
        raise TypeError(f"Second argument must be an integer, got {type(b).__name__}")
    return a * b
if __name__ == '__main__':
    result = multiply_integers(42, 10)
    print(result)