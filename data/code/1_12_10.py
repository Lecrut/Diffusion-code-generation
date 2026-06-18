def filter_valid_weights(weight_list):
    """
    Filters a list of weight measurements to return only valid positive numerical values.
    
    Args:
        weight_list (list[str]): A list of strings representing potential weights.
        
    Returns:
        list[float]: A new list containing floats that are valid and positive numbers.
                    Invalid entries or conversion errors result in silent skipping.
    """
    filtered_weights = []
    for item in weight_list:
        try:
            # Attempt to convert the string to a float
            num_weight = float(item)
            
            # Check if the number is strictly positive (greater than 0)
            if num_weight > 0:
                filtered_weights.append(num_weight)
        except ValueError:
            # Silently ignore items that cannot be converted to floats or are not numeric strings
            continue
            
    return filtered_weights

if __name__ == '__main__':
    # Hard-coded sample values containing valid positive weights, negative numbers, 
    # non-numeric strings, and zero.
    sample_data = [
        "10.5",      # Valid
        "-3.2",      # Invalid (negative)
        "",          # Invalid (empty string -> ValueError or 0.0 which is not positive if parsed as float('') fails)
        "abc",       # Invalid
        "   ",       # Invalid
        "0",         # Invalid (not strictly positive)
        "25.75",     # Valid
        "NaN",       # Invalid
    ]

    result = filter_valid_weights(sample_data)
    
    print(f"Input: {sample_data}")
    print(f"Output: {result}")