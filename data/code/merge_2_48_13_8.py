def safe_divide(dividend: float | int, divisor: float | int) -> float:
    try:
        dividend = float(dividend)
        divisor = float(divisor)
        if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
            raise TypeError("Inputs must be numeric.")
        if divisor == 0.0:
            return None
        result = dividend / divisor
    except ValueError as e:
        print(f"Error: {e}")
        return None
    return result
if __name__ == '__main__':
    test_cases = [
        (10, 2),
        (5.5, 3),
        ("abc", 4),
        (7, "xyz"),
        (8, 0),
        (-9, -3)
    ]
    for a in test_cases:
        print(f"Dividing {a[0]} by {a[1]}:", safe_divide(a[0], a[1]))