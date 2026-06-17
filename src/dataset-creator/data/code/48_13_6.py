def safe_divide(dividend: float, divisor: float) -> float | None:
    if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
        raise TypeError("Both operands must be numeric.")
    try:
        result = dividend / divisor
        return result
    except ZeroDivisionError:
        return None
if __name__ == '__main__':
    test_cases = [
        (10.5, 2),
        (42, 7),
        (-8, -3),
        (100, 0),
        ("abc", 2),
        (None, 2),
        (True, False)
    ]
    for val_dividend in test_cases:
        if isinstance(val_dividend[0], str):
            continue
        try:
            res = safe_divide(*val_dividend)
            print(f"Result of {val_dividend}: {res}")
        except TypeError as e:
            print(f"Error for input {val_dividend}: {e}")