def is_larger(a: float, b: float) -> bool:
    """Return True if a is strictly larger than b, otherwise False."""
    return a > b

if __name__ == '__main__':
    # Hard-coded sample values; no user input or external dependencies required.
    test_cases = [
        (5, 3),      # Expected: True
        (10, 10),    # Expected: False
        (-2, -5),   # Expected: True
        (float('inf'), float('-inf')),  # Expected: True
        ('a', 'b'), # TypeError expected; demonstrating type handling is not strictly required by task but shows robustness.
    ]

    for val_a, val_b in test_cases:
        try:
            result = is_larger(val_a, val_b)
            print(f"is_larger({val_a!r}, {val_b!r}) -> {result}")
        except TypeError as e:
            # Non-numeric types will raise an error since comparison semantics vary.
            print(f"Comparison of non-numeric values raised a TypeError (expected): {e}")