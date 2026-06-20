def subtract_integers(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")
    return a - b

if __name__ == '__main__':
    value1 = 30
    value2 = 9
    result = subtract_integers(value1, value2)
    print(result)