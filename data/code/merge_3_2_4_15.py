def parse_volumes(volume_string: str) -> list[float]:
    """
    Parses a comma-separated string of volume values into a list of floats.
    
    Args:
        volume_string (str): A string containing numbers separated by commas, 
                             potentially surrounded by whitespace or newlines.
                             
    Returns:
        list[float]: A list of floating-point numbers extracted from the input string.
        
    Raises:
        ValueError: If any non-numeric value is found in the input string.
    
    Example:
        >>> parse_volumes("10, 20.5")
        [10.0, 20.5]
    """
    if not volume_string or not isinstance(volume_string, str):
        raise ValueError("Input must be a non-empty string.")

    # Split the string by commas and strip whitespace from each part
    parts = [part.strip() for part in volume_string.split(',')]
    
    float_values = []
    for i, part in enumerate(parts):
        if not part:  # Skip empty strings resulting from consecutive commas or leading/trailing delimiters
            continue
            
        try:
            value = float(part)
            float_values.append(value)
        except ValueError as e:
            raise ValueError(f"Invalid numeric input at index {i}: '{part}'. Error details: {e}")

    return float_values

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    sample_input = "10, 20.5\n30, invalid, 40.1"
    
    try:
        result = parse_volumes(sample_input)
        print("Successfully parsed volumes:", result)
        
        # Additional test case with all valid numbers on one line
        sample_input_2 = "100, 200, 300"
        result_2 = parse_volumes(sample_input_2)
        print("Second test result:", result_2)
        
    except ValueError as ve:
        print(f"Error encountered during parsing: {ve}")