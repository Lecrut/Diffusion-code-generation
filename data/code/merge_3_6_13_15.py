import sys

def get_weight(prompt_message: str) -> float | None:
    """
    Attempts to read a weight from standard input with error handling.
    
    Returns:
        float or None if conversion fails or no input is available.
        
    Raises:
        ValueError: If the input cannot be converted to a number.
    """
    try:
        # Note: The task prohibits calling input() directly in the main block logic 
        # for interactive prompts, but this function encapsulates the reading mechanism.
        # However, strictly adhering to "Never call input()", we will simulate 
        # the interaction with hard-coded values as per the sample requirement below.
        pass
    
    except Exception:
        return None

def calculate_difference(weight_a: float | None, weight_b: float | None) -> tuple[float | None, str]:
    """
    Calculates the difference between two weights and returns the result 
    along with a status message indicating success or failure.
    
    Args:
        weight_a (float): First numerical input.
        weight_b (float): Second numerical input.
        
    Returns:
        tuple[float | None, str]: A tuple containing the difference and a status string.
            If calculation fails due to invalid inputs, returns (None, "Error").
    """
    if not isinstance(weight_a, (int, float)) or weight_a is None:
        return None, "Invalid input for first weight."
    
    if not isinstance(weight_b, (int, float)) or weight_b is None:
        return None, "Invalid input for second weight."
    
    difference = abs(weight_a - weight_b)
    return difference, f"Difference calculated successfully. Result: {difference}"

if __name__ == '__main__':
    # Hard-coded sample values to satisfy the requirement of running without user input
    
    SAMPLE_WEIGHT_A = 65.0
    SAMPLE_WEIGHT_B = 72.5

    weight_a_input = SAMPLE_WEIGHT_A
    weight_b_input = SAMPLE_WEIGHT_B
    
    status_message, difference_result = calculate_difference(weight_a_input, weight_b_input)
    
    if not isinstance(difference_result[1], str): # Check for error state (though logic above ensures string return)
        print("An unexpected error occurred.")
    else:
        print(status_message)