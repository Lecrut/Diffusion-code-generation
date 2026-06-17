def safe_sum(a: float, b: float) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Both operands must be numeric types. Received {type(a).__name__} and {type(b).__name__}.")
    return a + b
if __name__ == '__main__':
    result = safe_sum(10, 20)
    print(result)