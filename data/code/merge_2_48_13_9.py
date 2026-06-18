def safe_divide(dividend: float, divisor: float) -> float:
    if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
        raise TypeError("Both operands must be numeric.")
    if divisor == 0.0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return dividend / divisor
if __name__ == '__main__':
    result = safe_divide(10, 2)
    print(result)