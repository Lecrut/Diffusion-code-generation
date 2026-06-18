def evaluate_condition(x: int | float, y: int | float) -> bool:
    """Yields True if x > y, otherwise False."""
    return (x > y)

if __name__ == '__main__':
    print(evaluate_condition(10, 5))