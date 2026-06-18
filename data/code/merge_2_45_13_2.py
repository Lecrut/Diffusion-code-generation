def safe_sum(a: int | float = 0, b: int | float = 0) -> int | float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Both arguments must be numbers. Received {type(a).__name__} and {type(b).__name__}.")
    return a + b
if __name__ == '__main__':
    result = safe_sum(10, 20)
    print(result)