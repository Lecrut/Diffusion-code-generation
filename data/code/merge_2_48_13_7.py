def safe_divide(dividend: float, divisor: float) -> float | None:
    try:
        if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
            raise TypeError("Inputs must be numeric.")
        if divisor == 0.0:
            return None
        result = dividend / divisor
        return round(result, 15)
    except Exception as e:
        print(f"Division error: {e}")
        return None
if __name__ == '__main__':
    test_cases = [
        (10.5, 2),
        (-4, -8),
        (7, 0),
        ("abc", 3),
        (None, 5),
        (True, True)
    ]
    for dividend, divisor in test_cases:
        output = safe_divide(dividend, divisor)
        print(f"{dividend} / {divisor} = {output}")