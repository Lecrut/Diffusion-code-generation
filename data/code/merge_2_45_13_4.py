def safe_sum(a: float, b: float) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both operands must be numeric types.")
    try:
        return a + b
    except Exception as e:
        raise RuntimeError(f"Arithmetic operation failed due to {type(e).__name__}: {e}") from None
if __name__ == '__main__':
    result = safe_sum(10, 20)
    print(result)