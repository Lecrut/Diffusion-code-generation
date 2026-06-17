import math
def safe_divide(dividend: float | int, divisor: float | int) -> float:
    if not isinstance(divisor, (int, float)):
        raise TypeError("Divisor must be an integer or float.")
    if not math.isfinite(dividend):
        raise ValueError("Invalid dividend value.")
    try:
        divisor = float(divisor)
    except OverflowError:
        raise ValueError("Overflow occurred during conversion of divisor to float.")
    if divisor == 0.0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return dividend / divisor
if __name__ == '__main__':
    result = safe_divide(10, 2)
    print(result)