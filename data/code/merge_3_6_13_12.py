import sys

def validate_input(input_str):
    """
    Validates that the input string can be converted to a float.
    
    Args:
        input_str (str): The user's raw input string.
        
    Returns:
        float: The numerical value of the string if valid, None otherwise.
    """
    try:
        return float(input_str)
    except ValueError as ve:
        print(f"Error: Invalid number format - {ve}. Please enter a numeric weight.")
        return None

def calculate_difference(weight1, weight2):
    """
    Calculates the simple difference between two weights.
    
    Args:
        weight1 (float): The first numerical weight.
        weight2 (float): The second numerical weight.
        
    Returns:
        float: The result of subtracting weight2 from weight1.
    """
    try:
        return abs(weight1 - weight2)
    except TypeError as te:
        print(f"Error: Both inputs must be valid numbers to calculate the difference.")
        raise

if __name__ == '__main__':
    # Sample values hardcoded for execution without user input or command-line arguments.
    sample_values = ["70", "85"]

    try:
        weight1_float = float(sample_values[0])
        weight2_float = float(sample_values[1])
        
        difference_result = calculate_difference(weight1_float, weight2_float)
        print(f"Simple Weight Difference: {difference_result}")
    except IndexError as ie:
        # Handles case where there aren't enough sample values provided.
        sys.stderr.write("Error: Not enough sample input data to proceed.\n")
        raise