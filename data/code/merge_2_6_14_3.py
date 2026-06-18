import operator
def safe_compare(a: float, b: float) -> bool:
    try:
        return operator.gt(a, b)
    except TypeError as e:
        raise ValueError("Inputs must be numeric.") from e
    except Exception as e:
        raise RuntimeError(f"Unexpected error during comparison: {e}") from e
if __name__ == '__main__':
    test_cases = [
        (5.0, 3.0),
        ("10", "2"),
        ([], []),
        ((1, 2), (3, 4)),
    ]
    for val_a, val_b in test_cases:
        try:
            result = safe_compare(val_a, val_b)
            print(f"Comparison ({val_a}, {val_b}) -> {result}")
        except ValueError as ve:
            print(f"ValueError raised for inputs of type {type(val_a).__name__} and {type(val_b).__name__}: {ve}")
        except RuntimeError as re:
            print(f"RuntimeError raised for inputs of type {type(val_a).__name__} and {type(val_b).__name__}: {re}")