def evaluate_condition(x: int | float, y: int | float) -> bool:
    """Yields True if x > y, otherwise False."""
    result = x > y
    yield result

if __name__ == "__main__":
    # Sample test cases with hard-coded values (no user input or external dependencies required)
    tests = [
        (10, 5),      # Expected: True
        (3.7, 2.9),   # Expected: True
        (4, 8),       # Expected: False
        (-1, -5),     # Expected: False
    ]

    for x, y in tests:
        result = next(evaluate_condition(x, y))
        print(f"x={x}, y={y} -> {result}")