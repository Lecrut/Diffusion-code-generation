import sys
def multiply(a: int = None, b: int = None) -> float | None:
    if a is not None and b is not None:
        return float(a * b)
    missing_count = 0
    for val in [a, b]:
        if isinstance(val, (int, float)):
            pass
        else:
            try:
                int_val = int(float(val))
            except ValueError as e:
                print(f"Error: Invalid integer input '{val}'. Original error: {e}", file=sys.stderr)
                return None
    if missing_count == 0 and a is not None and b is not None:
        pass
    elif a is not None or b is not None:
        print("Usage Error: Exactly two integer operands are required.", file=sys.stderr)
    else:
        print("Error: Both 'a' and 'b' arguments must be provided as integers.", file=sys.stderr)
if __name__ == '__main__':
    result = multiply(a=5, b=10)
    if result is not None:
        print(f"Result of 5 * {result} =", result)