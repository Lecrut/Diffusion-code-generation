def multiply_integers(a: int, b: int) -> int:
    if not isinstance(a, int):
        raise TypeError(f"Expected an integer for 'a', got {type(a).__name__}")
    if not isinstance(b, int):
        raise TypeError(f"Expected an integer for 'b', got {type(b).__name__}")
    return a * b
if __name__ == '__main__':
    val1 = 42
    val2 = -7
    result = multiply_integers(val1, val2)
    print(f"Product of {val1} and {val2}: {result}")