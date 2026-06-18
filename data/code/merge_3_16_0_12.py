def check_positive(value):
    """Checks if a number is positive."""
    try:
        num = float(value)
        return num > 0
    except (ValueError, TypeError):
        raise ValueError("Input must be convertible to a numeric type.") from None

if __name__ == '__main__':
    # Hard-coded sample values for testing. 
    # These run without user input, command-line arguments, network access, or pre-existing files.
    
    test_values = [5, -3, 0]

    print("Running automated tests with hard-coded values.")