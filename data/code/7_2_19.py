import re

def format_to_seconds(time_str: str) -> int:
    """
    Converts a time string in 'H:M:S' format to total seconds.
    
    Args:
        time_str (str): A string representing hours, minutes, and seconds separated by colons.
        
    Returns:
        int: The total duration in seconds.
        
    Raises:
        ValueError: If the input string does not match the expected 'H:M:S' format or contains invalid values.
    """
    # Pattern to match H:M:S where each part is a non-negative integer
    pattern = r'^(\d+):(\d+):(\d+)$'
    
    if not isinstance(time_str, str) or not time_str.strip():
        raise ValueError("Input must be a non-empty string.")
        
    # Remove leading/trailing whitespace
    clean_time = time_str.strip()
    
    match = re.match(pattern, clean_time)
    if not match:
        raise ValueError(f"Invalid format. Expected 'H:M:S', got '{clean_time}'.")
    
    hours = int(match.group(1))
    minutes = int(match.group(2))
    seconds = int(match.group(3))
    
    # Validation for reasonable time values (though technically H, M, S can be anything)
    if hours < 0 or minutes < 0 or seconds < 0:
        raise ValueError("Time components must be non-negative.")

    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    
    return total_seconds

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    samples = [
        "1:30:45",   # Expected output: 5445
        "2:45:00",   # Expected output: 9900
        "0:10:30"    # Expected output: 630
    ]

    for sample in samples:
        try:
            result = format_to_seconds(sample)
            print(f"{sample} -> {result} seconds")
        except ValueError as e:
            print(f"Error processing '{sample}': {e}")