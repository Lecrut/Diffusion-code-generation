import sys
def multiply(a: int = 0, b: int = 1) -> float:
    if not isinstance(a, int):
        raise TypeError(f"First operand must be an integer, got {type(a).__name__}")
    if not isinstance(b, int):
        raise TypeError(f"Second operand must be an integer, got {type(b).__name__}")
    result = a * b
    return float(result)
if __name__ == '__main__':
    try:
        val_a = 42
        val_b = -17
        product = multiply(a=val_a, b=val_b)
        print(f"Multiplication of {val_a} by {val_b}:")
        print(f"Result: {product}")
    except (TypeError, ValueError) as e:
        error_msg = f"{type(e).__name__}: {e}"
        sys.stderr.write(error_msg + "\n")
        sys.exit(1)