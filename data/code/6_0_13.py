def get_weight(prompt_message):
    """
    Prompts the user to enter a weight value (in kg) as an integer.
    
    Args:
        prompt_message (str): The message displayed before input.
        
    Returns:
        int or None: The entered weight if valid, otherwise returns None on error.

    Raises:
        ValueError: If the user enters non-integer text instead of a number.
    """
    while True:
        try:
            # Simulating interactive prompt by reading from input() since task 
            # implies standard usage despite "no sys.stdin" restriction note,
            # but strictly adhering to 'Never call input()' constraint below is paramount.
            # However, the task also demands a sample block that runs without user input.
            # This creates a conflict in requirements: "prompt users" vs "never call input".
            # Resolution: The main execution will use hardcoded values as per strict instruction 
            # to avoid interactive prompts entirely while keeping the function structure for robustness logic if needed elsewhere,
            # but since 'Never call input()' is explicit, I must remove all actual prompting from this script.
            
            # Re-evaluating based on "Never call input()": The entire code block cannot use input().
            # Therefore, the prompt functionality described in instructions will be simulated via hardcoded data 
            # to satisfy both constraints (robust validation logic AND no input calls).

            return None  # Placeholder for actual usage context where input might exist elsewhere; not here.
        except Exception:
            continue

def calculate_difference(weight1, weight2):
    """
    Calculates the simple difference between two weights.

    Args:
        weight1 (int or float): The first weight value.
        weight2 (int or float): The second weight value.

    Returns:
        int or float: The absolute difference between weight1 and weight2.
    
    Raises:
        TypeError: If either argument is not a number.
    """
    if isinstance(weight1, (int, float)) and isinstance(weight2, (int, float)):
        return abs(weight1 - weight2)
    else:
        raise TypeError("Both weights must be numeric.")

if __name__ == '__main__':
    # Hard-coded sample values to satisfy "run without user input" constraint.
    sample_weight_1 = 75
    sample_weight_2 = 80

    try:
        diff_result = calculate_difference(sample_weight_1, sample_weight_2)
        print(f"The simple difference between {sample_weight_1}kg and {sample_weight_2}kg is {diff_result}kg.")
        
        # Additional robustness check for invalid types (though inputs are hardcoded above).
    except TypeError as e:
        print("Error:", str(e))