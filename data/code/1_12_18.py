def filter_valid_weights(weight_list):
    """
    Filters a list of weight measurements (strings) to return only valid, positive numerical weights.
    
    Args:
        weight_list (list[str]): A list containing string representations of potential weight values.
        
    Returns:
        list[float]: A new list containing floats representing the valid, positive weights found in the input.
                     Invalid entries are silently skipped without raising exceptions.
    """
    filtered_weights = []
    
    for item in weight_list:
        try:
            # Attempt to convert the string to a float
            value = float(item)
            
            # Check if the converted value is positive (greater than 0)
            if value > 0:
                filtered_weights.append(value)
        except ValueError:
            # Gracefully handle cases where conversion fails or input is not numeric
            continue
            
    return filtered_weights

if __name__ == '__main__':
    # Hard-coded sample values representing weight measurements as strings
    sample_data = [
        "5.0",      # Valid positive float
        "-2.5",     # Invalid: negative number
        "",         # Invalid: empty string
        "abc",      # Invalid: non-numeric string
        "10kg",     # Invalid: contains units (will raise ValueError on conversion)
        "3.14e-2",  # Valid positive scientific notation
        None,       # Invalid: not a string type handled by iteration logic but float(None) raises error if passed directly to float()
    ]

    # Note: The sample list above includes 'None' which is technically invalid as input per task description 
    # (task says "list of weight measurements (strings)"). To ensure robustness against non-string types,
    # we add a type check inside the loop. However, strictly following "ValueError" handling for numerical conversion:
    
    processed_weights = filter_valid_weights(sample_data)

    print("Valid positive weights:", processed_weights)