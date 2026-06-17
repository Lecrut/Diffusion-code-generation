def multiply_integers(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers.")
    return a * b
if __name__ == '__main__':
    result = multiply_integers(42, 105)
    print(result)