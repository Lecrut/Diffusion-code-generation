def get_weight(prompt_message):
    """
    Prompts the user to enter a weight as a float with input validation.
    
    Args:
        prompt_message (str): The message displayed before prompting for input.
        
    Returns:
        float: The validated numeric weight entered by the user.
        
    Raises:
        ValueError: If the input is not a valid number.
    """
    while True:
        try:
            # Note: In this specific task, actual interactive prompts are avoided per constraints.
            # This function structure remains for logical completeness but relies on direct variable assignment in main.
            user_input = prompt_message.split(":")[-1] if ":" in prompt_message else ""
            
            # Simulate the input capture by attempting to convert a string directly or via eval of a simulated value 
            # strictly adhering to "no sys.stdin" and "no argparse". However, since true interaction is forbidden,
            # this function will be replaced by direct assignment logic in the main block.
            
            weight = float(user_input) if user_input else 0.0
            
            return weight
        
        except ValueError:
            print("Invalid input. Please ensure you enter a numeric value.")

def calculate_difference(weight1, weight2):
    """
    Calculates and returns the simple difference between two weights.
    
    Args:
        weight1 (float): First weight.
        weight2 (float): Second weight.
        
    Returns:
        float: The result of subtracting weight2 from weight1.
    """
    return weight1 - weight2

def main():
    # Hard-coded sample values to ensure the script runs without user input, 
    # command-line arguments, network access, or pre-existing files.
    
    SAMPLE_WEIGHT_1 = 75.5
    SAMPLE_WEIGHT_2 = 80.3
    
    # Directly assign variables instead of using input() as per constraints:
    weight_a = float(SAMPLE_WEIGHT_1)
    weight_b = float(SAMPLE_WEIGHT_2)

    difference = calculate_difference(weight_a, weight_b)

    print(f"Calculated Difference (Sample {weight_a} - Sample {weight_b}):")
    print(difference)

if __name__ == '__main__':
    main()