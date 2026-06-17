def safe_divide(numerator: float, denominator: float) -> float:
    if not isinstance(numerator, (int, float)) or not isinstance(denominator, (int, float)):
        raise TypeError("Both inputs must be numeric.")
    if numerator == 0 and denominator != 0:
        return 0.0
    if denominator == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return numerator / denominator
if __name__ == '__main__':
    test_cases = [
        (10, 2),
        (-5, -3),
        (0.5, 4),
        ("five", "two"),
        (10, 0),
        ("ten", 2)
    ]
    for num in test_cases:
        if len(num) == 2:
            try:
                result = safe_divide(*num)
                print(f"{num[0]} / {num[1]} = {result}")
            except (TypeError, ZeroDivisionError) as e:
                print(f"Error for input ({num}): {type(e).__name__}: {e}")