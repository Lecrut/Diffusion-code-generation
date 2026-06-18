def parse_volumes(volume_string: str) -> list[float]:
    """
    Parses a comma-separated string of volume values into a list of floats.
    
    Args:
        volume_string (str): A string containing numbers separated by commas, 
                             potentially with whitespace or non-numeric characters.
                             
    Returns:
        list[float]: A list of floating-point numbers extracted from the input string.
        
    Raises:
        ValueError: If a segment in the string cannot be converted to a float.
    """
    try:
        # Split the string by commas and strip whitespace from each part
        parts = [part.strip() for part in volume_string.split(',')]
        
        result = []
        for part in parts:
            if not part:  # Skip empty strings resulting from consecutive commas or leading/trailing commas
                continue
            
            try:
                value = float(part)
                result.append(value)
            except ValueError as e:
                raise ValueError(f"Invalid numeric input '{part}': {e}")
        
        return result
        
    except Exception as e:
        # Re-raise with a more descriptive message if an unexpected error occurs during splitting or processing
        raise RuntimeError(f"Error parsing volume string: {e}") from None

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    sample_input_1 = "50.5, 72.3, invalid, 98.0"
    sample_input_2 = "10, 20, 30"
    
    print("Sample Input 1:", repr(sample_input_1))
    try:
        volumes_1 = parse_volumes(sample_input_1)
        print("Parsed Volumes 1:", volumes_1)
    except ValueError as ve:
        print(f"Error processing Sample Input 1: {ve}")

    print("\nSample Input 2:", repr(sample_input_2))
    try:
        volumes_2 = parse_volumes(sample_input_2)
        print("Parsed Volumes 2:", volumes_2)
    except ValueError as ve:
        print(f"Error processing Sample Input 2: {ve}")

    # Test with extra whitespace and empty segments
    sample_input_3 = "1.0,   , 2.5,, 3.7"
    
    print("\nSample Input 3:", repr(sample_input_3))
    try:
        volumes_3 = parse_volumes(sample_input_3)
        print("Parsed Volumes 3:", volumes_3)
    except ValueError as ve:
        print(f"Error processing Sample Input 3: {ve}")