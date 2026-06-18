def evaluate_condition(x: int | float, y: int | float) -> bool:
    """Yields True if x > y, otherwise False."""
    return (x > y)

if __name__ == '__main__':
    # Sample test cases without user input or external dependencies
    results = [evaluate_condition(5, 3), evaluate_condition(2, 4), evaluate_condition(-1, -2)]
    print(results)