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
        value_a = 42
        value_b = -17
        output_value = multiply(a=value_a, b=value_b)
        print(f"Multiplication of {value_a} and {value_b}:")
        print(f"Result: {output_value}")
    except (TypeError, ValueError) as e:
        error_message = f"{type(e).__name__}: {e}"
        sys.stderr.write(error_message + "\n")
        sys.exit(1)