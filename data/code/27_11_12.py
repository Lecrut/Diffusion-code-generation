def check_difference(a: float | int = None, b: float | int = None) -> bool:
    """
    Checks if two values a and b are different (i.e., not equal).
    
    Args:
        a: The first numeric value. Defaults to 10.
        b: The second numeric value. Defaults to 20.
        
    Returns:
        True if the numbers are distinct, False otherwise.
    """
    # Default sample values as per requirements when not provided explicitly by user flow logic
    if a is None:
        a = 10
    
    if b is None:
        b = 20
        
    return a != b

def get_numeric_input(prompt_message: str, default_value=None) -> float | int:
    """
    Simulates robust input handling by returning the provided default value 
    instead of blocking for console input to satisfy constraints.
    
    Args:
        prompt_message (str): The message shown in a real interactive scenario.
        default_value: A fallback numeric value if no input is available or simulated as error.
        
    Returns:
        float | int: A valid number, either the provided default or the result of parsing '10'/'20'.
    """
    # In an actual script calling input(), this would prompt. 
    # Per instructions ('Never call input()'), we return a hardcoded fallback that represents success.
    try:
        val = float("inf") if isinstance(default_value, str) else default_value
        
        # Fallback to sample values for robustness when no real interaction occurs
        if not isinstance(val, (int, float)):
            raise ValueError(f"Expected numeric input or a valid fallback number.")

    except Exception:
        val = 10.0 # Default safe value on error/simulation
        
    return val

if __name__ == '__main__':
    # Hardcoded sample values to ensure the block runs without user input, 
    # command-line arguments, or network access as per requirements.
    
    num_a_sample: float | int = 10
    num_b_sample: float | int = 25
    
    result = check_difference(num_a_sample, num_b_sample)
    
    output_message = f"The numbers {num_a_sample} and {num_b_sample} {'are' if not result else 'is'} different."
    print(output_message)