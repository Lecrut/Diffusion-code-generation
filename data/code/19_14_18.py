def evaluate_condition(x: int | float, y: int | float) -> bool:
    """Yields True if x is strictly greater than y, otherwise False."""
    return (x > y)

if __name__ == '__main__':
    # Sample execution with hard-coded values
    result = evaluate_condition(10, 5)
    assert result is True

    result2 = evaluate_condition(3.7, 4.2)
    assert result2 is False