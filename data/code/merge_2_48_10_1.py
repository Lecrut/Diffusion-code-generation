import sys
def safe_divide(a: float, b: float) -> float | None:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both operands must be numeric.")
    if b == 0.0:
        return None
    return a / b
if __name__ == '__main__':
    num1 = 25
    num2 = 4
    try:
        result = safe_divide(num1, num2)
        print(result) if result is not None else print("Division by zero.")
    except TypeError as e:
        print(f"Error: {e}", file=sys.stderr)