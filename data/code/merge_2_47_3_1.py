import sys
def multiply(a: int = 0, b: int = 1) -> int:
    if not isinstance(a, int):
        raise TypeError(f"First operand must be an integer, got {type(a).__name__}")
    if not isinstance(b, int):
        raise TypeError(f"Second operand must be an integer, got {type(b).__name__}")
    return a * b
if __name__ == '__main__':
    try:
        result = multiply(42, 8)
        print(result)
    except (TypeError, ValueError) as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)