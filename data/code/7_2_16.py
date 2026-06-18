import re

def parse_time_to_seconds(time_str):
    """
    Converts a time string in 'H:M:S' format to total seconds.
    
    Args:
        time_str (str): Time string in the format H:M:S
        
    Returns:
        int: Total duration in seconds
        
    Raises:
        ValueError: If the input format is invalid or contains non-numeric values
    
    Examples:
        >>> parse_time_to_seconds('1:30:45')
        5445
        >>> parse_time_to_seconds('2:10:00')
        7400
    """
    pattern = r'^(\d+):(\d+):(\d+)$'
    match = re.match(pattern, time_str.strip())
    
    if not match:
        raise ValueError(f"Invalid time format. Expected 'H:M:S', got '{time_str}'")
    
    hours = int(match.group(1))
    minutes = int(match.group(2))
    seconds = int(match.group(3))
    
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    
    return total_seconds

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    test_cases = [
        '1:30:45',
        '2:10:00',
        '0:45:30',
        '5:9:8'
    ]
    
    print("Time Conversion Results:")
    for time_str in test_cases:
        try:
            total_seconds = parse_time_to_seconds(time_str)
            formatted_output = f"{time_str} -> {total_seconds}s"
            print(formatted_output)
            
            # Verification of calculation logic
            h, m, s = map(int, time_str.split(':'))
            expected = (h * 3600) + (m * 60) + s
            assert total_seconds == expected, "Calculation mismatch"
        except ValueError as e:
            print(f"Error processing '{time_str}': {e}")