import sys
def divide_numbers(a: float, b: float) -> float:
    try:
        coerced_a = float(str(a))
        coerced_b = float(str(b))
        return coerced_a / coerced_b
    except ZeroDivisionError:
        raise ValueError("Division by zero is not allowed.")
    except (ValueError, TypeError) as e:
        raise RuntimeError(f"Invalid input types or values: {e}")
if __name__ == '__main__':
    value_x = 10.5
    value_y = 2.3
    try:
        result = divide_numbers(value_x, value_y)
        print(f"{value_x} / {value_y} = {result:.4f}")
    except ValueError as ve:
        print(str(ve), file=sys.stderr)
    except RuntimeError as re:
        print(str(re), file=sys.stderr)