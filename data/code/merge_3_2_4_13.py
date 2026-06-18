def parse_volumes(volume_string: str) -> list[float]:
    """
    Parses a comma-separated string of volume values into a list of floats.
    
    Args:
        volume_string (str): A string containing numbers separated by commas, 
                             potentially surrounded by whitespace or newlines.
        
    Returns:
        list[float]: A list of floating-point numbers representing the parsed volumes.
        
    Raises:
        ValueError: If any non-numeric value is encountered in the input string.
    
    Example:
        >>> parse_volumes("10, 20.5, thirty")
        Traceback (most recent call last):
            ...
        ValueError: Invalid numeric value 'thirty' found at index 3.
        
        >>> parse_volumes("5, 6")
        [5.0, 6.0]
    """
    if not volume_string or not isinstance(volume_string, str):
        raise ValueError("Input must be a non-empty string.")

    # Split the string by commas and strip whitespace from each part
    parts = [part.strip() for part in volume_string.split(',')]
    
    floats = []
    for index, part in enumerate(parts):
        if not part:  # Skip empty strings resulting from consecutive commas or trailing comma
            continue
        
        try:
            value = float(part)
            floats.append(value)
        except ValueError as e:
            raise ValueError(f"Invalid numeric value '{part}' found at index {index}.")
    
    return floats

if __name__ == '__main__':
    # Hard-coded sample values to test the function without external input or files.
    sample_input_1 = "5, 6, 7"
    sample_input_2 = "100, twenty, -3.14"
    
    print("Sample Input 1:", repr(sample_input_1))
    try:
        result_1 = parse_volumes(sample_input_1)
        print(f"Parsed Result 1: {result_1}")
    except ValueError as e:
        print(f"Error parsing Sample Input 1: {e}")

    print("\nSample Input 2:", repr(sample_input_2))
    try:
        result_2 = parse_volumes(sample_input_2)
        print(f"Parsed Result 2: {result_2}")
    except ValueError as e:
        print(f"Error parsing Sample Input 2: {e}")

    # Test with empty string handling (though the function skips empty parts, 
    # this ensures robustness against leading/trailing spaces or newlines)
    sample_input_3 = "   , 1.5 , \n 2.0,"
    print(f"\nSample Input 3: {repr(sample_input_3)}")
    try:
        result_3 = parse_volumes(sample_input_3)
        print(f"Parsed Result 3: {result_3}")
    except ValueError as e:
        print(f"Error parsing Sample Input 3: {e}")

    # Test with invalid input to demonstrate error handling
    sample_invalid = "1, abc, 2"
    print(f"\nSample Invalid Input: {repr(sample_invalid)}")
    try:
        result_invalid = parse_volumes(sample_invalid)
        print(f"Parsed Result (should not happen): {result_invalid}")
    except ValueError as e:
        print(f"Expected error occurred for invalid input: {e}")