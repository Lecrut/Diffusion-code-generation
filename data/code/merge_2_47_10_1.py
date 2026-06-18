def multiply_integers(a: int, b: int) -> int:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numeric.")
    return a * b
if __name__ == '__main__':
    result = multiply_integers(-5, 10)
    print(result)