import operator
def safe_compare(a: float | int, b: float | int) -> bool:
    try:
        return operator.gt(a, b)
    except TypeError as e:
        raise ValueError(f"Non-numeric input detected for comparison at {a} vs {b}") from e
if __name__ == '__main__':
    result1 = safe_compare(5.0, 3.0)
    print(result1)
    try:
        _ = safe_compare("ten", "five")
    except ValueError as ve:
        print(f"Error caught: {ve}")
    result2 = safe_compare(-1, -2)
    print(result2)