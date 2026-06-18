def filter_valid_weights(weight_list):
    """
    Takes a list of weight measurements (strings) and returns a new list 
    containing only valid, positive numerical weights. Handles potential ValueError exceptions gracefully by skipping invalid entries.
    
    Args:
        weight_list (list[str]): List of strings representing weight measurements.
        
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
            # Gracefully handle cases where conversion fails or input is not numeric
            continue
            
    return result

if __name__ == '__main__':
    sample_weights = [
        "5.5", 
        "-2.3", 
        "", 
        "abc123", 
        "+7.0", 
        42,   # Note: This will cause a TypeError if passed directly as int in the loop above without conversion check first, but task specifies input is strings. Let's ensure robustness for mixed types just in case, though spec says list of weight measurements (strings).
    ]

    # Correction based on strict requirement "list of weight measurements (strings)" 
    # to avoid unexpected behavior if non-string elements slip through:
    
    cleaned_sample = []
    for item in sample_weights:
        if isinstance(item, str):
            try:
                val = float(item)
                if val > 0:
                    cleaned_sample.append(val)
            except ValueError:
                pass

    # Re-implementing logic to strictly follow "list of strings" input while being robust against non-string inputs in the sample block for demonstration purposes.
    
    def safe_filter(weights):
        filtered = []
        for w in weights:
            try:
                num = float(w) if isinstance(w, str) else w
                # If it was already a number and positive, keep it; 
                # Note: The prompt implies strings, but handling non-strings gracefully is good practice.
                # However, strict adherence to "list of ... (strings)" means we expect strings.
                # We will assume the input list contains only strings as per spec description for filtering logic.
                
                if isinstance(w, str):
                    val = float(w)
                    if val > 0:
                        filtered.append(val)
            except ValueError:
                continue
        return filtered

    final_result = safe_filter(sample_weights)
    
    print(f"Input sample weights (mixed/invalid included for test): {sample_weights}")
    print(f"Filtered valid positive weights: {final_result}")