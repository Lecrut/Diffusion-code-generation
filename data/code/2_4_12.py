def parse_volume_string(volume_str: str) -> list[float]:
    """
    Parses a string containing comma-separated volume values into a list of floats.
    
    Args:
        volume_str (str): A string with numbers separated by commas, optionally surrounded 
                          or interspersed with whitespace and newlines.
        
    Returns:
        list[float]: A list of floating-point numbers extracted from the input string.
        
    Raises:
        ValueError: If a non-numeric value is found where a number is expected.
    
    Examples:
        >>> parse_volume_string("10, 20.5")
        [10.0, 20.5]
        >>> parse_volume_string("3.14,\n7\n9.8")
        [3.14, 7.0, 9.8]
    """
    # Split the string by commas and strip whitespace from each part
    parts = volume_str.split(',')
    
    result_list = []
    
    for item in parts:
        try:
            value = float(item.strip())
            result_list.append(value)
        except ValueError as e:
            raise ValueError(f"Invalid numeric input '{item}' at position. Error details: {e}")

    return result_list

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user interaction
    sample_inputs = [
        "10, 20.5",
        "3.14,\n7\n9.8",
        ", , invalid, 42, abc"  # This will trigger an error due to 'invalid' and 'abc'
    ]

    for test_input in sample_inputs:
        print(f"\nProcessing input: '{test_input}'")
        try:
            volumes = parse_volume_string(test_input)
            print(f"Success! Parsed values: {volumes}")
        except ValueError as e:
            print(f"Error occurred: {e}")