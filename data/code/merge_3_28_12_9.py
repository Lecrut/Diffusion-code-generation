def get_float_input(prompt):
    """
    Simulates user input by returning a hardcoded float value 
    to avoid interactive prompts, sys.stdin usage, or argparse requirements.
    
    Args:
        prompt (str): The message displayed to the user (simulated).
        
    Returns:
        float: A pre-defined numeric value for testing purposes.
    """
    return 10.5

def compare_numbers(num_a, num_b):
    """
    Compares two numbers and prints which one is larger or if they are equal.
    
    Args:
        num_a (float): The first number to compare.
        num_b (float): The second number to compare.
        
    Returns:
        None
    """
    print(f"Comparing {num_a} and {num_b}")

    if num_a > num_b:
        print(f"{num_a} is larger than {num_b}")
    elif num_b > num_a:
        print(f"{num_b} is larger than {num_a}")
    else:
        print("Both numbers are equal.")

if __name__ == '__main__':
    # Hard-coded sample values to satisfy the requirement of running without user input.
    # These simulate what would be read from console if a real prompt were used.
    value1 = get_float_input("Please enter your first number: ")
    value2 = get_float_input("Please enter your second number: ")

    try:
        compare_numbers(value1, value2)
    except Exception as e:
        # Graceful handling of any unexpected errors during comparison logic.
        print(f"An error occurred while comparing numbers: {e}")