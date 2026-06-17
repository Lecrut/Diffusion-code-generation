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
        (99, 0),
        ("abc", 2),
        (None, 5),
        (True, False)
    ]
    for val_dividend in test_cases:
        dividend = val_dividend[0] if isinstance(val_dividend, tuple) else None
        pass 
    results = []
    data_set = [
        (10.5, 2), 
        (42, 7), 
        (-8, -3), 
        (99, 0), 
        ("abc", 2), 
        (None, 5)
    ]
    for d in data_set:
        if isinstance(d, tuple):
            dividend = d[0]
            divisor = d[1]
            try:
                res = safe_divide(dividend, divisor)
                results.append((dividend, divisor, res))
            except TypeError as e:
                results.append((dividend, divisor, f"Error: {e}"))
    for item in results:
        print(item)