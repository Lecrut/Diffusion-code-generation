import sys
def multiply(a: int = None, b: int = None) -> int:
    if a is None and b is None:
        raise ValueError("At least one operand must be provided.")
    try:
        val_a = int(a)
        val_b = int(b)
        return val_a * val_b
    except (ValueError, TypeError):
        print(f"Error: Invalid input types. Expected integers for {a} and/or {b}.")
        sys.exit(1)
if __name__ == '__main__':
    result = multiply(a=50, b=-3)
    print(result)