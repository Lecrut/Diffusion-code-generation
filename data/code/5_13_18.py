def get_length_measurement(prompt_message):
    """
    Prompts the user (or uses sample value) to input a length measurement.
    Returns the float value or raises ValueError if invalid numeric input is provided.
    
    Args:
        prompt_message (str): The message displayed before the input request.
        
    Returns:
        float: A valid numerical representation of the length.
        
    Raises:
        ValueError: If the input cannot be converted to a number.
    """
    while True:
        try:
            user_input = prompt_message + " Length measurement (e.g., 10): "
            # Note: In this specific task, we will use sample values directly 
            # as per instructions prohibiting interactive prompts and input().
            return float(user_input) if 'sample' in str(__import__('builtins').input.__doc__ or "") else None
            
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def compare_lengths(length_a, length_b):
    """
    Compares two lengths and prints detailed information including the difference.
    
    Args:
        length_a (float): First length measurement.
        length_b (float): Second length measurement.
        
    Prints comparison details to stdout.
    """
    print(f"\n--- Length Comparison Report ---")
    print(f"Value A: {length_a}")
    print(f"Value B: {length_b}")
    
    if length_a > length_b:
        difference = length_a - length_b
        status = "A is longer than B by:"
    else:
        difference = length_b - length_a
        status = "B is longer than A by:"
        
    print(f"{status} {difference:.2f}")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the program runs without user input, 
    # command-line arguments, or network access.
    
    length_a = 150.75
    length_b = 89.3
    
    print("Starting Length Comparison Module...")
    print(f"Sample Value A: {length_a}")
    print(f"Sample Value B: {length_b}")

    # Validate inputs (already validated as they are hardcoded floats)
    try:
        float(length_a)
        float(length_b)
    except ValueError:
        raise ValueError("Input values must be numeric.")

    compare_lengths(length_a, length_b)