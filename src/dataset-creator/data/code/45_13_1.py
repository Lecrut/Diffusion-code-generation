def safe_sum(a: float | int = None, b: float | int = None) -> float:
    if a is not None and b is not None:
        try:
            return float(a) + float(b)
        except TypeError as e:
            raise ValueError(f"Invalid types for addition. Expected numeric values (int or float). Received {type(a).__name__} and {type(b).__name__}.") from e
    elif a is None and b is not None:
        try:
            return float(b) + 0.0
        except TypeError as e:
            raise ValueError(f"Invalid types for addition. Expected numeric values (int or float). Received only {type(b).__name__}.") from e
    elif a is not None and b is None:
        try:
            return float(a) + 0.0
        except TypeError as e:
            raise ValueError(f"Invalid types for addition. Expected numeric values (int or float). Received only {type(a).__name__}.") from e
    else:
        raise ValueError("Both operands must be provided.")
if __name__ == '__main__':
    result = safe_sum(10, 20)
    print(result)