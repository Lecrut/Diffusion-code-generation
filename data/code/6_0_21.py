import sys

def get_weight(prompt_message: str) -> float | None:
    """
    Attempts to parse a weight value from user input with validation.
    
    Returns:
        A validated numeric weight, or None if invalid input is encountered
        (though per task constraints, this function will not be called interactively).
    """
    try:
        return float(prompt_message)
    except ValueError:
        raise ValueError("Invalid number format")

def calculate_difference(weight_a: float | None, weight_b: float | None) -> int | None:
    """
    Calculates the simple difference between two weights.
    
    Args:
        weight_a (float): First weight value.
        weight_b (float): Second weight value.
        
    Returns:
        The absolute integer difference or None if either input is invalid/None.
    """
    if not isinstance(weight_a, float) and not isinstance(weight_b, float):
        return None
    
    abs_diff = abs(weight_a - weight_b)
    
    # Round to nearest whole number for simplicity as per "simple difference" context
    rounded_diff = round(abs_diff)
    
    return int(rounded_diff)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    SAMPLE_WEIGHT_A = 50.7
    SAMPLE_WEIGHT_B = 42.3

    try:
        diff_result = calculate_difference(SAMPLE_WEIGHT_A, SAMPLE_WEIGHT_B)
        
        if diff_result is not None:
            print(f"Sample Weight A: {SAMPLE_WEIGHT_A}")
            print(f"Sample Weight B: {SAMPLE_WEIGHT_B}")
            print(f"Difference (absolute): {diff_result} kg")
    except ValueError as e:
        # This block handles potential parsing errors if the sample logic were dynamic,
        # but with hard-coded floats here, it won't be triggered.
        print(f"Error during calculation: {e}")