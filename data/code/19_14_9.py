def evaluate_condition(x: int | float, y: int | float) -> bool:
    """Yields True if x > y, otherwise False."""
    result = x > y
    yield result

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    for val in evaluate_condition(10, 5):
        print(val)