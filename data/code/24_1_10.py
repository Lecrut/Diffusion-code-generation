def is_negative(value):
    """Returns True if value is less than zero, False otherwise."""
    return value < 0

if __name__ == '__main__':
    # Hard-coded sample values to test the function without external input
    samples = [-5.0, -1, 0, 3.14, float('-inf'), float('inf')]

    for num in samples:
        result = is_negative(num)
        print(f"is_negative({num}) = {result}")