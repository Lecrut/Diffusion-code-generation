import sys
def safe_divide(a: float, b: float) -> float | None:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both operands must be numeric.")
    if b == 0.0:
        return None
    result = a / b
    return result
if __name__ == '__main__':
    numerator = 10.5
    denominator = 2.3
    try:
        quotient = safe_divide(numerator, denominator)
        if quotient is not None:
            print(f"{numerator} / {denominator} = {quotient}")
        else:
            print("Division by zero detected.")
    except TypeError as e:
        print(f"Input error: {e}", file=sys.stderr)
    except ZeroDivisionError:
        print("Attempted division by zero.", file=sys.stderr)