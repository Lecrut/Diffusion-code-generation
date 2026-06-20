def subtract_values(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers.")
    return a - b

if __name__ == '__main__':
    result = subtract_values(10, 5)
    print(result)