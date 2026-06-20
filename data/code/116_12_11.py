def sum_floats(a: float, b: float, c: float) -> float:
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise ValueError("All inputs must be numbers")
    return a + b + c

if __name__ == '__main__':
    result = sum_floats(1.1, 2.2, 3.3)
    print(result)