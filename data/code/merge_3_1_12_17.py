def filter_valid_weights(weight_list):
    """
    Takes a list of weight measurements (strings) and returns a new list 
    containing only valid, positive numerical weights. Handles potential ValueError exceptions gracefully.
    
    Args:
        weight_list (list[str]): A list of strings representing weight measurements.
        
    Returns:
        list[float]: A list of floats corresponding to the valid, positive numeric inputs from the input list.
    """
    filtered_weights = []
    
    for item in weight_list:
        try:
            # Attempt to convert string to float and check if it's a number (including negative/zero)
            num_value = float(item)
            
            # Check if the value is positive (> 0.0)
            if num_value > 0.0:
                filtered_weights.append(num_value)
        except ValueError:
            # Gracefully handle cases where conversion fails or input is not a valid number
            continue
            
    return filtered_weights

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction, network access, or file dependencies.
    sample_data = [
        "50.5",      # Valid positive weight
        "-10.2",     # Invalid (negative)
        "",          # Invalid (empty string)
        "abc",       # Invalid (non-numeric)
        " 30.0 ",    # Valid positive weight with whitespace (float handles this)
        "0",         # Invalid (zero is not positive)
        "1e2",       # Valid scientific notation
        None,        # This will cause a ValueError during float(None), handled gracefully below if needed, 
                     # but since the input type hint says list[str], we assume strings. However, to be robust:
    ]

    # Note: The function expects strings based on docstring and task description ("list of weight measurements (strings)").
    # If None or non-string types slip in during runtime execution without explicit handling outside this scope, 
    # float() will raise ValueError which is caught. However, strict adherence to "strings" implies we might not see None.
    # To ensure robustness against unexpected non-convertible objects while maintaining the 'string' contract expectation:
    
    safe_sample_data = [str(w) if w else "" for w in sample_data]

    result_weights = filter_valid_weights(safe_sample_data)

    print("Filtered valid positive weights:", result_weights)