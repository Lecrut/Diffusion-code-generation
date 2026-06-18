def parse_volumes(volume_string: str) -> list[float]:
    """
    Takes a string containing comma-separated volume values and returns 
    a list of floating-point numbers.
    
    Includes error handling for non-numeric inputs by raising a ValueError 
    with an informative message if any value cannot be converted to float.

    Args:
        volume_string (str): A string representing comma-separated volume values, e.g., "10.5, 20.3, abc"

    Returns:
        list[float]: List of floating-point numbers parsed from the input string.

    Raises:
        ValueError: If any value in the string is not a valid number.
    """
    try:
        # Split the string by comma and strip whitespace from each element
        parts = [part.strip() for part in volume_string.split(',')]
        
        volumes = []
        for i, part in enumerate(parts):
            if not part:  # Handle empty strings resulting from consecutive commas or leading/trailing commas
                continue
            try:
                volumes.append(float(part))
            except ValueError as e:
                raise ValueError(f"Invalid numeric value at index {i}: '{part}'") from e
        
        return volumes

    except Exception as e:
        # Catch any unexpected exceptions during splitting or processing
        if not isinstance(volume_string, str):
            raise TypeError("Input must be a string.") from e
        raise ValueError(f"Failed to parse volume values due to an error: {str(e)}")

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements (no user input or CLI args)
    sample_input = "10.5, 20.3, 30.7"

    try:
        result = parse_volumes(sample_input)
        print(f"Parsed volumes from '{sample_input}': {result}")
        
        # Test case with an invalid number to demonstrate error handling
        sample_invalid = "15.0, xyz, 25.5"
        try:
            invalid_result = parse_volumes(sample_invalid)
            print("Unexpected success for invalid input.")
        except ValueError as ve:
            print(f"Caught expected error for invalid input '{sample_invalid}': {ve}")

    except Exception as e:
        # This block handles errors from the main execution logic itself if needed, 
        # though parse_volumes should handle most parsing exceptions.
        raise RuntimeError("Error in sample execution.") from e