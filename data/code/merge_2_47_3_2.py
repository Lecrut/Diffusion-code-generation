import sys
def multiply(a: int = 0, b: int = 1) -> int:
    if not isinstance(a, int):
        raise TypeError(f"First operand must be an integer, got {type(a).__name__}")
    if not isinstance(b, int):
        raise TypeError(f"Second operand must be an integer, got {type(b).__name__}")
    result = a * b
    return result
if __name__ == '__main__':
    try:
        value_a = 42
        value_b = -73
        product = multiply(a=value_a, b=value_b)
        print(f"Product of {value_a} and {value_b}:")
        print(product)
    except (TypeError, ValueError) as e:
        error_message = f"{type(e).__name__}: {e}"
        sys.stderr.write(error_message + "\n")
        sys.exit(1)