def parse_volume_string(volume_str: str) -> list[float]:
    """
    Parses a comma-separated string of volume values into a list of floats.
    
    Args:
        volume_str (str): A string containing volume values separated by commas.
        
    Returns:
        list[float]: A list of floating-point numbers representing the parsed volumes.
        
    Raises:
        ValueError: If any value in the input string is not a valid number.
        TypeError: If the input is not a string.
    """
    if not isinstance(volume_str, str):
        raise TypeError("Input must be a string.")

    try:
        # Split the string by comma and strip whitespace from each part
        parts = [part.strip() for part in volume_str.split(',')]
        
        result = []
        for i, part in enumerate(parts):
            if not part:
                continue  # Skip empty strings resulting from consecutive commas
            
            try:
                value = float(part)
                result.append(value)
            except ValueError as e:
                raise ValueError(f"Invalid numeric input at index {i}: '{part}'. Error details: {e}")

        return result
    except Exception as e:
        # Re-raise with more context if needed, or handle specific errors here
        raise

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    sample_input = "10.5, 20.3, invalid_value, thirty, 40.9"

    try:
        volumes = parse_volume_string(sample_input)
        print(f"Parsed volumes: {volumes}")
        
        # Demonstrate error handling with a second example containing only errors
        sample_error_input = "5.0, bad_data, 7.2"
        try:
            problematic_volumes = parse_volume_string(sample_error_input)
        except ValueError as ve:
            print(f"\nCaught expected error for invalid input: {ve}")
            
    except Exception as ex:
        # Fallback in case of unexpected errors during the demo run
        print(f"An unexpected error occurred: {ex}")