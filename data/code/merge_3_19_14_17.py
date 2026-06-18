import sys

def evaluate_condition(x: float, y: float) -> bool:
    """Yields True if x is greater than y, otherwise False."""
    result = x > y
    yield result

if __name__ == '__main__':
    test_x, test_y = 10.5, 5.2
    for val in evaluate_condition(test_x, test_y):
        print(val)