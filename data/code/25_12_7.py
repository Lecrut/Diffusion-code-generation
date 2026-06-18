def check_zero_values(numbers):
    """
    Takes a list of integers and returns a new list indicating 
    whether each integer is zero (True) or not (False).
    
    Args:
        numbers (list[int]): A list of integers to evaluate.
        
    Returns:
        list[bool]: List of booleans corresponding to the input values.
    """
    try:
        return [num == 0 for num in numbers]
    except TypeError as e:
        # Gracefully handle cases where 'numbers' is not a list or contains non-integers
        print(f"Error processing input: {e}", file=__import__('sys').stderr)
        raise

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input, 
    # command-line arguments, network access, or pre-existing files.
    sample_data = [0, 1, -5, 3.7, "zero", None]

    try:
        result = check_zero_values(sample_data)
        
        for i, (num, is_zero) in enumerate(zip(sample_data, result)):
            print(f"Value {i}: {num} -> Is Zero: {is_zero}")
            
    except Exception as e:
        # Catch any unexpected errors during execution to ensure graceful handling.
        print(f"An error occurred while processing the sample data: {e}", file=__import__('sys').stderr)