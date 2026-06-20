def subtract_integers(a: int, b: int) -> int:
    if not isinstance(a, int):
        raise ValueError("First input must be an integer")
    if not isinstance(b, int):
        raise ValueError("Second input must be an integer")
    return a - b

if __name__ == '__main__':
    result = subtract_integers(10, 5)
    print(result)