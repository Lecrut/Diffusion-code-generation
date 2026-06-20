def subtract_numbers(a: float, b: float) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")
    return a - b

if __name__ == '__main__':
    result = subtract_numbers(25.0, 10.0)
    print(result)