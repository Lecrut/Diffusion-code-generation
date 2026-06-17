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
        print(f"{num1} divided by {num2} is {result}")
    except TypeError as e:
        print(f"Error: Invalid input type. {e}", file=sys.stderr)
        sys.exit(1)
    except ZeroDivisionError:
        print("Warning: Division by zero.", file=sys.stderr)