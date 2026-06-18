def evaluate_condition(x: int | float, y: int | float) -> bool:
    """Yields True if x > y, otherwise False."""
    return (x > y)

if __name__ == '__main__':
    results = [evaluate_condition(10, 5), evaluate_condition(3.5, 4.2)]
    print(results)