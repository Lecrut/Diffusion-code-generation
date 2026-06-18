import sys
def safe_divide(numerator: float, denominator: float) -> tuple[float | None]:
    try:
        coerced_numerator = float(int(float(numerator))) if isinstance(numerator, (int, str)) else numerator
        coerced_denominator = float(int(float(denominator))) if isinstance(denominator, (int, str)) else denominator
        result = coerced_numerator / coerced_denominator
    except ZeroDivisionError:
        return None
    except TypeError as e:
        print(f"Type error occurred: {e}", file=sys.stderr)
        sys.exit(1)
    return float(result)
if __name__ == '__main__':
    val_a = 42.5
    val_b = "7"
    output_value = safe_divide(val_a, val_b)
    if output_value is not None:
        print(f"{val_a} / {val_b} = {output_value}")
    else:
        print("Division failed due to zero denominator.")