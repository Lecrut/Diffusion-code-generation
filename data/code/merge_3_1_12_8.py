def filter_valid_weights(weight_list):
    """
    Takes a list of weight measurements (strings) and returns a new list 
    containing only valid, positive numerical weights. Handles potential ValueError exceptions gracefully.
    
    Args:
        weight_list (list[str]): A list of strings representing weight measurements.
        
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
            # Gracefully handle cases where conversion fails or item is not numeric
            continue
            
    return result

if __name__ == '__main__':
    # Hard-coded sample values including valid numbers, invalid strings, and non-positive numbers
    sample_weights = [
        "5.0", 
        "-3.2", 
        "", 
        "abc123", 
        "+7.89", 
        0, 
        "   ", 
        "invalid!", 
        "0.0"
    ]

    # Process the sample list and print the result
    valid_weights = filter_valid_weights(sample_weights)
    
    if not isinstance(valid_weights[0], float):
        # Fallback for any edge case where input might be mixed types in a real scenario, 
        # though our function ensures only floats are appended. This check is defensive.
        print("Error: Unexpected type in result list.")
    else:
        print(f"Valid positive weights found: {valid_weights}")