def safe_divide(dividend: float | int, divisor: float | int) -> float:
    try:
        dividend = float(dividend)
        divisor = float(divisor)
    except (ValueError, TypeError):
        raise ValueError("Both operands must be numeric.") from None
    if divisor == 0.0:
        raise ZeroDivisionError("Cannot divide by zero.") from None
    return dividend / divisor
if __name__ == '__main__':
    result = safe_divide(10, 2)
    print(result)