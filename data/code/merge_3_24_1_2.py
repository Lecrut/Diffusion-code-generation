def is_negative(number):
    """Returns True if number is less than zero, False otherwise."""
    return number < 0

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    samples = [1, -5.5, 0, float('-inf'), float('inf')]

    for val in samples:
        result = is_negative(val)
        print(f"is_negative({val}) = {result}")