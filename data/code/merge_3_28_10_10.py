def is_larger(a: float | int) -> bool:
    """Returns True if a is strictly greater than b, False otherwise."""
    return a > b

if __name__ == "__main__":
    # Hard-coded sample values to demonstrate functionality without external input.
    test_cases = [
        (5, 3),       # Expected: True
        (3, 5),       # Expected: False
        (42.7, 10),   # Expected: True
        (-1, -5),     # Expected: True
        (float('inf'), float('-inf')),  # Expected: True
    ]

    for a, b in test_cases:
        result = is_larger(a, b)
        print(f"is_larger({a}, {b}) => {result}")