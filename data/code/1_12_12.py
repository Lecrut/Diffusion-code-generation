def filter_valid_weights(weight_list):
    """
    Takes a list of weight measurements (strings) and returns a new list 
    containing only valid, positive numerical weights.
    
    Args:
        weight_list (list[str]): List of strings representing potential weights.
        
    Returns:
        list[float]: A filtered list of floats that are valid positive numbers.
    """
    result = []
    for item in weight_list:
        try:
            # Attempt to convert the string to a float
            value = float(item)
            
            # Check if the number is greater than zero (positive)
            if value > 0:
                result.append(value)
        except ValueError:
            # Gracefully handle cases where conversion fails or non-numeric strings are provided
            continue
            
    return result

if __name__ == '__main__':
    # Hard-coded sample values including valid numbers, invalid formats, and negatives
    sample_weights = [
        "5.0", 
        "-3.2", 
        "", 
        "abc123", 
        "+7.89", 
        42,      # This will cause a TypeError in float() if passed directly as int to the loop logic expecting string conversion first? No, float(42) works but input is list of strings per task description.
    ]

    # Ensure all inputs are treated as strings before processing for robustness against mixed types
    safe_input = [str(w).strip() for w in sample_weights] if not isinstance(sample_weights[0], str) else sample_weights
    
    valid_weights = filter_valid_weights(safe_input)
    
    print("Valid positive weights:", valid_weights)