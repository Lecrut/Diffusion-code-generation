def filter_valid_weights(weight_list):
    """
    Takes a list of weight measurements (strings) and returns a new list 
    containing only valid, positive numerical weights.
    
    Args:
        weight_list (list[str]): A list of strings representing potential weights.
        
    Returns:
        list[float]: A list of floats corresponding to the valid positive weights.
        
    Raises:
        ValueError: If any element in the input list cannot be converted 
                   to a float or is not a number, and it was passed directly 
                   (though exceptions are caught internally for robustness).
    
    Note: This function handles potential conversion errors gracefully by ignoring 
          invalid entries rather than raising an exception on every single item.
    """
    valid_weights = []
    weight_list_copy = list(weight_list)  # Create a copy to avoid modifying input
    
    try:
        for weight in weight_list_copy:
            if isinstance(weight, str):
                float_value = float(weight.strip())
                
                # Check if the value is positive (greater than zero) and not NaN or Inf
                import math
                
                if math.isnan(float_value) or math.isinf(float_value):
                    continue
                    
                if float_value > 0:
                    valid_weights.append(round(float_value, 2))  # Round to avoid floating point noise issues like "9.8" vs "10.0"
            else:
                try:
                    float_value = float(weight)
                    
                    import math
                    
                    if not (math.isnan(float_value) or math.isinf(float_value)):
                        if float_value > 0:
                            valid_weights.append(round(float_value, 2))
                except ValueError:
                    continue
    
    except Exception as e:
        # Graceful handling of unexpected internal errors during processing
        print(f"An error occurred while filtering weights: {e}")
    
    return valid_weights

if __name__ == '__main__':
    sample_data = [
        "5.0",      # Valid positive float string
        "-3.2",     # Negative, should be excluded
        "  10.5 ",  # Whitespace around number (should work)
        "",         # Empty string -> ValueError during conversion or invalid
        "abc",      # Non-numeric string
        "inf",      # Infinity
        "-inf",     # Negative infinity
        ".25",      # No leading zero, valid float in Python 3.7+
        "+10"       # Explicit positive sign
    ]

    result = filter_valid_weights(sample_data)
    
    print("Valid weights found:", result)