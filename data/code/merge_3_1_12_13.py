def filter_valid_weights(weight_strings):
    """
    Takes a list of weight measurements (strings) and returns a new list 
    containing only the valid, positive numerical weights as floats.
    
    Parameters:
        weight_strings (list[str]): List of strings representing potential weights.
        
    Returns:
        list[float]: A list of valid, positive float values found in the input.
                     Invalid entries are silently skipped instead of raising exceptions.
    """
    filtered_weights = []
    
    for item in weight_strings:
        try:
            # Attempt to convert string to float
            weight_value = float(item)
            
            # Check if the value is positive (greater than 0) and not NaN or Inf
            import math
            
            if math.isnan(weight_value):
                continue
                
            if math.isinf(weight_value):
                continue
                
            if weight_value <= 0:
                continue
                
            filtered_weights.append(weight_value)
            
        except ValueError:
            # Gracefully handle cases where the string cannot be converted to a float
            pass
            
    return filtered_weights

if __name__ == '__main__':
    # Sample input data containing valid weights, invalid formats, negatives, and edge cases
    sample_data = [
        "10.5",           # Valid positive number
        "-5.2",           # Negative (should be excluded)
        "invalid",         # Non-numeric string
        "   3.14    ",     # Whitespace padding (valid after strip/float conversion)
        "",               # Empty string -> ValueError during float()
        "inf",            # Infinity
        "-0.0",           # Negative zero (treated as non-positive by <= check for clarity, but mathematically 0)
        "1e3",            # Scientific notation
    ]

    result = filter_valid_weights(sample_data)
    
    print("Filtered valid positive weights:", result)