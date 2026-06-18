def check_negative(value: int) -> str:
    """Check if a given integer is negative and return a descriptive string."""
    if value < 0:
        return f"The entered value {value} is negative."
    else:
        return f"The entered value {value} is not negative."

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or external dependencies.
    test_values = [10, -5, 0]
    
    for num in test_values:
        result_message = check_negative(num)
        print(result_message)