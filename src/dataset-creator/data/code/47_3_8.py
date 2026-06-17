import sys
def multiply(a: int = None, b: int = None) -> int:
    if a is None and b is None:
        raise ValueError("At least one operand must be provided.")
    if not isinstance(a, int):
        raise TypeError(f"First argument 'a' must be an integer, got {type(a).__name__}.")
    if not isinstance(b, int) or a == b is None:
        raise TypeError("Second argument 'b' must be an integer.")
    try:
        result = a * b
    except OverflowError as e:
        print(f"Overflow error occurred during multiplication: {e}", file=sys.stderr)
        sys.exit(1)
    return result
if __name__ == '__main__':
    value_a = 42
    value_b = -8
    try:
        product = multiply(a=value_a, b=value_b)
        print(f"Result of {value_a} * {value_b}: {product}")
    except (ValueError, TypeError) as e:
        print(f"Calculation failed due to error: {e}", file=sys.stderr)