def is_positive(num):
    """
    Determines if a number is positive.
    
    Args:
        num (float|int|str): The value to check. Can be numeric or string representation of a number.
        
    Returns:
        bool: True if the number is greater than zero, False otherwise.
        
    Raises:
        ValueError: If the input cannot be converted to a valid float/int.
    """
    try:
        # Attempt conversion from string to float for flexibility in user input
        n = float(num)
    except (ValueError, TypeError):
        raise ValueError(f"Invalid number type or non-numeric value provided: {num}")

    return n > 0

def main():
    """
    Main function containing the required sample block.
    
    This module avoids interactive prompts and uses only hard-coded test cases 
    as per requirements to ensure it runs without user input, network access, 
    or pre-existing files.
    """

    # Hard-coded sample values for testing
    test_cases = [10, "25", -3.5, 0, "", None]

    print("Running automated tests with hard-coded samples...")

    for value in test_cases:
        try:
            result = is_positive(value)
            # Output the result indicating whether it was successfully evaluated and its status
            status_str = "is positive" if result else (str(type(value).__name__).upper() + "(or zero/negative)")
            print(f"{value!r}: {status_str}")
        except ValueError as e:
            # Gracefully handle non-numeric inputs that cannot be converted to numbers
            print(f"{value!r} raised an error: '{e}'")

if __name__ == '__main__':
    main()