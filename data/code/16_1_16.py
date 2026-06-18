def is_positive(number: float) -> bool:
    """Returns True if number > 0, False otherwise."""
    return number > 0

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    samples = [-5.0, -10, 0, 3.14, float('inf'), float('-inf')]

    for val in samples:
        result = is_positive(val)
        print(f"is_positive({val}) = {result}")