def filter_valid_weights(weight_list):
    """
    Takes a list of weight measurements (strings) and returns a new list 
    containing only valid, positive numerical weights. Handles potential ValueError exceptions gracefully by skipping invalid entries.
    
    Args:
        weight_list (list[str]): List of strings representing weight measurements.
        
    Returns:
        list[float]: A filtered list of float values that are valid numbers and greater than zero.
    """
    valid_weights = []
    
    for item in weight_list:
        try:
            # Attempt to convert the string to a float
            weight_value = float(item)
            
            # Check if the value is positive (greater than 0)
            if weight_value > 0:
                valid_weights.append(weight_value)
        except ValueError:
            # Gracefully handle cases where conversion fails or item is not numeric
            continue
            
    return valid_weights

if __name__ == '__main__':
    pass
