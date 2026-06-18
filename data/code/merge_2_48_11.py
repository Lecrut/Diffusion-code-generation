def safe_divide(dividend: float | int, divisor: float | int) -> float:
    try:
        dividend = float(dividend)
        divisor = float(divisor)
        if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
            raise TypeError("Both arguments must be numeric.")
        if divisor == 0.0:
            raise ZeroDivisionError("Divisor cannot be zero.")
    except ValueError as ve:
        raise TypeError(f"Invalid input type: {ve}") from None
    return dividend / divisor
if __name__ == '__main__':
    result = safe_divide(10, 2)
    print(result)