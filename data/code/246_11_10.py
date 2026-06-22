def sum_with_precision(a: float, b: float) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")
    return a + b

if __name__ == '__main__':
    try:
        result = sum_with_precision(0.1, 0.2)
        print(result)
    except ValueError as e:
        print(e)