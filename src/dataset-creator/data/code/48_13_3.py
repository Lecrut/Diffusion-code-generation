def safe_divide(dividend: float, divisor: float) -> float | None:
    if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
        raise TypeError("Both operands must be numeric.")
    if divisor == 0.0:
        return None
    result = dividend / divisor
    return result
if __name__ == '__main__':
    test_cases = [
        (10, 2),
        (5, 0),
        ("a", 2),
        (3.5, -7),
        (None, 4)
    ]
    for val in test_cases:
        try:
            res = safe_divide(*val)
            print(f"Result of {val}: {res}")
        except Exception as e:
            print(f"Error with {val}: {e}")