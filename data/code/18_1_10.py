def is_greater(a: float, b: float) -> bool:
    """Returns True if a > b, otherwise False."""
    return a > b

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    results = [is_greater(10.5, 3), is_greater(-5, -2), is_greater(42, 99), is_greater(float('inf'), float('-inf'))]
    print(results)