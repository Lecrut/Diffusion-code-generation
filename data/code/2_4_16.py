def parse_volume_string(volume_str: str) -> list[float]:
    """
    Parses a string containing comma-separated volume values into a list of floats.
    
    Args:
        volume_str (str): A string with numbers separated by commas, e.g., "10, 20.5, thirty".
        
    Returns:
        list[float]: A list of floating-point numbers parsed from the input string.
        
    Raises:
        ValueError: If any part of the input cannot be converted to a float (e.g., non-numeric strings).
    
    Example:
        >>> parse_volume_string("10, 20")
        [10.0, 20.0]
        >>> parse_volume_string("3.5, four, 7")
        ValueError: Invalid input encountered at index 4 ('four'). Cannot convert to float.
    """
    try:
        # Split the string by comma and strip whitespace from each part
        parts = [part.strip() for part in volume_str.split(',')]
        
        result = []
        for i, part in enumerate(parts):
            if not part:  # Handle empty strings resulting from consecutive commas or trailing comma
                continue
            
            try:
                value = float(part)
                result.append(value)
            except ValueError as e:
                raise ValueError(f"Invalid input encountered at index {i} ('{part}'). Cannot convert to float.") from e
        
        return result
    
    except Exception as e:
        # Re-raise with context if an unexpected error occurs during processing
        raise RuntimeError(f"Error parsing volume string: {e}")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        "10, 20.5",           # Standard numeric inputs
        "-5, -3.7, 0",       # Including negative numbers and zero
        "100,",               # Trailing comma (should be handled gracefully)
        ", , 42",            # Leading/trailing commas with empty segments in between
    ]

    for i, test_input in enumerate(test_cases):
        print(f"Test case {i + 1}: Input = '{test_input}'")
        try:
            volumes = parse_volume_string(test_input)
            print(f"Parsed result: {volumes}")
        except ValueError as ve:
            print(f"Error occurred: {ve}")
        
    # Example of an invalid input to demonstrate error handling
    invalid_input = "10, abc, 30"
    print("\nTest case (Invalid): Input = '10, abc, 30'")
    try:
        volumes = parse_volume_string(invalid_input)
        print(f"Parsed result: {volumes}")
    except ValueError as ve:
        print(f"Error occurred: {ve}")