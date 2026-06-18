def safe_divide(dividend: float | int, divisor: float | int) -> float:
    if not isinstance(divisor, (int, float)):
        raise TypeError("Divisor must be a numeric type.")
    try:
        dividend = float(dividend)
        divisor = float(divisor)
    except ValueError as e:
        raise ValueError(f"Invalid input types for division. {e}") from None
    if not isinstance(dividend, (int, float)):
        raise TypeError("Dividend must be a numeric type.")
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return dividend / divisor
if __name__ == '__main__':
    result = safe_divide(10.5, 2)
    print(result)