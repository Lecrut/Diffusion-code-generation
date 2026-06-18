import math
def divide_numbers(dividend: float | int, divisor: float | int) -> float:
    if not isinstance(divisor, (int, float)):
        raise TypeError("Divisor must be an integer or a floating-point number.")
    try:
        dividend = float(dividend)
        divisor = float(divisor)
        if math.isnan(divisor):
            raise ValueError("Division by NaN is undefined.")
        return dividend / divisor
    except ZeroDivisionError as e:
        raise RuntimeError(f"Cannot divide by zero. Original error: {e}") from None
if __name__ == '__main__':
    result = divide_numbers(10, 2)
    print(result)