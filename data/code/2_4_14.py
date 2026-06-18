def parse_volume_string(volume_str: str) -> list[float]:
    """
    Parses a string containing comma-separated volume values into a list of floats.
    
    Args:
        volume_str (str): A string with volume numbers separated by commas, e.g., "10.5, 20.3, thirty".
        
    Returns:
        list[float]: A list of floating-point numbers parsed from the input string.
        
    Raises:
        ValueError: If any value in the string is not a valid number or if the format is incorrect (e.g., missing comma).
    
    Example:
        >>> parse_volume_string("10, 20")
        [10.0, 20.0]
        
        >>> parse_volume_string("a, b")
        ValueError: Invalid input encountered at index 'b' - not a valid number.
    """
    
    if not volume_str or not isinstance(volume_str, str):
        raise ValueError("Input must be a non-empty string.")

    values = []
    parts = [part.strip() for part in volume_str.split(',')]

    try:
        for i, part in enumerate(parts):
            # Skip empty strings resulting from consecutive commas or leading/trailing spaces if handled by strip above
            if not part:
                continue
            
            num_value = float(part)
            
            # Check for NaN (Not a Number), which can occur with inputs like "nan" or "inf" depending on context, 
            # though the task implies standard numeric validation. We'll treat non-finite numbers as errors based on typical volume requirements.
            if not num_value.is_finite():
                raise ValueError(f"Invalid input encountered at index {i} - value '{part}' is not a finite number.")

            values.append(num_value)
    except ValueError:
        # This catches cases where the string part cannot be converted to float (e.g., "thirty")
        try:
            idx = parts.index(part) if 'not' in str(type(volume_str)) else 0 
            # Re-calculate index properly for error message clarity without complex logic errors above
            raise ValueError(f"Invalid input encountered at index {parts.index(part)} - '{part}' is not a valid number.") from None
        except (ValueError, IndexError):
            raise ValueError("Failed to parse numeric values in the string.")

    return values

if __name__ == '__main__':
    # Hard-coded sample inputs for testing without user interaction or external dependencies.
    
    test_cases = [
        "10.5, 20.3",           # Standard case with spaces after commas
        "100,200,300",          # No spaces between numbers and commas
        "invalid, 5.5, abc",   # Contains non-numeric strings to trigger error handling logic in loop or split check if needed (though current implementation handles 'abc' via float conversion)
    ]

    for test_input in test_cases:
        try:
            result = parse_volume_string(test_input)
            print(f"Input: '{test_input}'")
            print("Output:", result)
            print("-" * 20)
        except ValueError as e:
            print(f"Error processing input '{test_input}': {e}")
            print("-" * 20)

    # Specific test for error handling with non-numeric string inside the list logic.
    # Note: The current implementation uses float() directly which raises ValueError immediately on 'abc'.
    # To demonstrate specific index reporting, we rely on Python's default behavior or adjust if strict indexing is required by modifying the loop slightly above.
    
    try:
        bad_input = "10, twenty"
        result_bad = parse_volume_string(bad_input)
    except ValueError as e:
        print(f"Demonstrated error handling for non-numeric input:")
        print(e)