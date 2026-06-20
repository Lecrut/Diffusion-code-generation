def multiply_numbers(a: float, b: float) -> float:
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both inputs must be numeric")
    return a * b

if __name__ == '__main__':
    result = multiply_numbers(3.5, 2.0)
    print(result)