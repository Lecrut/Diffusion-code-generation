def divide_numbers(dividend: float | int, divisor: float | int) -> float:
    if not isinstance(divisor, (int, float)):
        raise TypeError("Divisor must be a numeric type.")
    try:
        dividend = float(dividend)
        divisor = float(divisor)
    except ValueError as e:
        raise ValueError(f"Both operands must support conversion to float: {e}") from e
    if divisor == 0.0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return dividend / divisor
if __name__ == '__main__':
    result = divide_numbers(10, 2)
    print(result)