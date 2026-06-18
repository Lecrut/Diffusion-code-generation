import re

def parse_volumes(volume_string: str) -> list[float]:
    """
    Parses a string containing comma-separated volume values into a list of floats.
    
    Args:
        volume_string (str): A string with numbers separated by commas, e.g., "10.5, 20, -3"
        
    Returns:
        list[float]: List of floating-point numbers extracted from the input string.
        
    Raises:
        ValueError: If any value in the input cannot be converted to a float (e.g., contains non-numeric characters).
    
    Example:
        >>> parse_volumes("1, 2.5, three")
        Traceback (most recent call last):
            ...
        ValueError: Invalid volume found at index 3: 'three'
        
        >>> parse_volumes("0.1,-0.2,0.3")
        [0.1, -0.2, 0.3]
    """
    volumes = []
    
    # Split the string by commas and strip whitespace from each part
    parts = volume_string.split(',')
    
    for index, value in enumerate(parts):
        stripped_value = value.strip()
        
        if not stripped_value:
            raise ValueError(f"Empty value found at index {index}")
            
        try:
            float_val = float(stripped_value)
            volumes.append(float_val)
        except ValueError as e:
            # Check for non-numeric input like "abc" or mixed types like "1.0, 2a"
            raise ValueError(f"Invalid volume found at index {index}: '{stripped_value}'") from e
            
    return volumes

if __name__ == '__main__':
    # Hard-coded sample values without user interaction
    test_cases = [
        "10.5, 20.0, -3",
        "0.1,-0.2,0.3",
        "invalid input here",
        ", , ,",
        "42"
    ]

    for i, sample in enumerate(test_cases):
        print(f"\nTest case {i + 1}: '{sample}'")
        try:
            result = parse_volumes(sample)
            print(f"Parsed volumes: {result}")
        except ValueError as e:
            print(f"Error occurred: {e}")