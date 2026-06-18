def safe_sum(a: float, b: float) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Both operands must be numeric types. Received {type(a).__name__} and {type(b).__name__}.")
    try:
        return a + b
    except Exception as e:
        if "unsupported operand type(s)" in str(e):
            raise ValueError("Numeric addition failed due to incompatible mathematical operations.") from None
        else:
            raise
if __name__ == '__main__':
    result = safe_sum(10, 20)
    print(f"Sum of {10} and {20}: {result}")