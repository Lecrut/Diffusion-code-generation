def safe_divide(dividend: float, divisor: float) -> float | None:
    if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
        raise TypeError("Both operands must be numeric.")
    try:
        result = dividend / divisor
    except ZeroDivisionError:
        return None
    return result
if __name__ == '__main__':
    test_cases = [
        (10.5, 2),
        (7, 3),
        ("abc", 4),
        (8, "xyz"),
        (9, 0),
        (-5, -2)
    ]
    for dividend, divisor in test_cases:
        try:
            res = safe_divide(dividend, divisor)
            print(f"Dividing {dividend} by {divisor}:") if isinstance(res, float) else None
            if res is not None:
                print("Result:", res)
            else:
                print("Error: Division by zero.")
        except TypeError as e:
            print(f"Type Error for inputs ({dividend}, {divisor}):", str(e))