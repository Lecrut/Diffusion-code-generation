def evaluate_condition(x: float, y: float) -> bool:
    """Yields True if x is greater than y, otherwise False."""
    yield x > y

if __name__ == '__main__':
    results = list(evaluate_condition(10.5, 3.2))
    print(results[0])