import operator as op
def safe_gt(a: float | int, b: float | int) -> bool:
    try:
        return op.gt(a, b)
    except TypeError:
        raise ValueError("Inputs must be numeric.") from None
if __name__ == '__main__':
    test_cases = [
        (10.5, 2),
        ("abc", "xyz"),
        ([1], [2]),
        (None, 5)
    ]
    for val_a, val_b in test_cases:
        try:
            result = safe_gt(val_a, val_b)
            print(f"{val_a} > {val_b}: {result}")
        except ValueError as e:
            print(f"Error comparing {val_a} and {val_b}: {e}")