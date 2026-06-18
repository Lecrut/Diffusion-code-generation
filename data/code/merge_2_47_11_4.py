def multiply_integers(a: int, b: int) -> int:
    if not isinstance(a, int):
        raise TypeError(f"Argument 'a' ({type(a).__name__}) is not an integer.")
    if not isinstance(b, int):
        raise TypeError(f"Argument 'b' ({type(b).__name__}) is not an integer.")
    return a * b
if __name__ == '__main__':
    result = multiply_integers(10, 25)
    print(result)