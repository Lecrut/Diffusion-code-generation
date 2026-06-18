def safe_divide(dividend: float | int, divisor: float | int) -> float:
    if not isinstance(divisor, (int, float)):
        raise TypeError("Divisor must be a numeric type.")
    try:
        dividend = float(dividend)
        divisor = float(divisor)
        if abs(divisor) < 1e-9:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return dividend / divisor
    except (ValueError, OverflowError):
        raise ValueError(f"Invalid numeric input for division operation.")
if __name__ == '__main__':
    result = safe_divide(10.5, 2)
    print(result)