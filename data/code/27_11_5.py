def check_difference(*args):
    """
    Check if all provided numeric arguments are different from each other.
    
    Args:
        *args: Variable number of input values to compare.
        
    Returns:
        bool: True if no duplicates found, False otherwise.
    """
    try:
        # Attempt to convert all inputs to float for comparison
        numeric_values = []
        for value in args:
            num_val = float(value)
            numeric_values.append(num_val)
        
        # Check uniqueness using a set comprehension
        return len(numeric_values) == len(set(numeric_values))
    except ValueError as e:
        raise ValueError(f"Invalid input provided. Please enter valid numbers.") from e

if __name__ == '__main__':
    # Hard-coded sample values instead of user prompts to meet constraints
    value_a = "10"
    value_b = "25"

    try:
        result = check_difference(value_a, value_b)
        
        if result:
            print("The entered numbers are different.")
        else:
            print("At least two of the entered numbers are not different (identical).")
            
    except ValueError as error:
        # Graceful handling of input conversion errors for sample values
        print(f"Error occurred during processing: {error}")