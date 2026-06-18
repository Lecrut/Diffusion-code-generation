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
        print(f"Multiplication of {val_a} and {val_b}:")
        print(f"Result: {product}")
        try:
            bad_result = multiply(a="42", b=5)
        except TypeError as e:
            print(f"\nCaught expected error in sample case:")
            print(e)
    except Exception as unexpected_error:
        sys.stderr.write(f"Unexpected runtime error occurred:\n{unexpected_error}\n")
        sys.exit(1)