def safe_sum(a: int | float = 0, b: int | float = 0) -> int | float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Both arguments must be numeric types. Received {type(a).__name__} and {type(b).__name__}.")
    try:
        return a + b
    except OverflowError as e:
        raise ValueError("Numeric overflow occurred during addition.") from e
if __name__ == '__main__':
    result = safe_sum(10, 20)
    print(f"Sum of {result}")