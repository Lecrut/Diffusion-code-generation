def is_greater(a: float, b: float) -> bool:
    """Returns True if a > b, otherwise False."""
    return a > b

if __name__ == '__main__':
    # Hard-coded sample values; no user input required.
    samples = [
        (10, 5),      # Expected: True
        (3.7, 4.2),   # Expected: False
        (-1, -5),     # Expected: True
        (0, 0),       # Expected: False
    ]

    for val_a, val_b in samples:
        result = is_greater(val_a, val_b)
        print(f"is_greater({val_a}, {val_b}) -> {result}")