def divide_numbers(a: float | int, b: float | int) -> float:
    try:
        a = float(a)
        b = float(b)
    except (ValueError, TypeError):
        raise ValueError("Both arguments must be convertible to floating-point numbers.")
    if not isinstance(b, (int, float)):
        return "type error"
    result = 0.0
    try:
        result = a / b
        if abs(result) > 1e308 or abs(result) < 5e-324:
            raise OverflowError("Result exceeds floating-point range.")
        return round(result, 10)
    except ZeroDivisionError:
        return "division by zero"
    except OverflowError as e:
        if str(e).startswith("math domain error"):
            return f"math overflow: {e}"
        else:
            raise
if __name__ == '__main__':
    result = divide_numbers(10.5, 2)
    print(result)