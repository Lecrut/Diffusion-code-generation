def evaluate_condition(x: int | float, y: int | float) -> bool:
    """Yields True if x > y, otherwise False."""
    yield x > y

if __name__ == '__main__':
    results = list(evaluate_condition(10, 5))
    print(results[0])