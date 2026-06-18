import re

def time_difference_seconds(time_str1: str, time_str2: str) -> int:
    """
    Calculates the difference in total seconds between two time strings.
    
    The function expects input strings to be formatted as 'HH:MM:SS'.
    If a string is missing any component (e.g., 'H:M:S' or just 'M'), 
    it attempts to parse available components, padding with zeros where necessary.
    
    Args:
        time_str1 (str): First time point in HH:MM:SS format.
        time_str2 (str): Second time point in HH:MM:SS format.
        
    Returns:
        int: The difference between the two times in seconds (time1 - time2).
           If either string is invalid, a ValueError is raised.
           
    Raises:
        ValueError: If input strings do not match expected patterns or contain non-numeric values.
    """
    
    # Regex pattern to capture hours, minutes, and seconds allowing for optional parts
    # Matches groups like H:M:S, HH:M:S, etc., ensuring numeric content only
    time_pattern = re.compile(r'^(\d{1,2})(?::(\d{1,2}))?(?::(\d{1,2}))?$')
    
    def parse_time(time_str: str) -> int:
        """Converts a single time string to total seconds."""
        
        match = time_pattern.match(time_str.strip())
        if not match:
            raise ValueError(f"Invalid time format: {time_str}")
            
        hours, minutes, seconds = map(int, [match.group(1), match.group(2) or '0', match.group(3) or '0'])
        
        # Validate ranges (hours < 24 is a strict requirement for standard clocks)
        if not (0 <= hours < 24):
            raise ValueError(f"Hours must be between 0 and 23, got {hours}")
            
        return hours * 3600 + minutes * 60 + seconds
    
    try:
        total_seconds_1 = parse_time(time_str1)
        total_seconds_2 = parse_time(time_str2)
        
        diff = total_seconds_1 - total_seconds_2
        
        # Ensure the result is an integer (it should be by construction, but explicit cast for safety)
        return int(diff)
    except ValueError as e:
        raise ValueError(f"Error processing time strings: {e}")

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    test_cases = [
        ("12:30:45", "08:15:30"),  # Standard case with all components
        ("9:05", "7:40"),          # Case with missing seconds (assumed 0)
        ("23:59:59", "00:00:01"), # Edge case near midnight wrap-around logic check
    ]
    
    print("Time Difference Calculator Results:")
    for t1, t2 in test_cases:
        try:
            diff = time_difference_seconds(t1, t2)
            print(f"From {t1} to {t2}: {diff:+d} seconds")
        except ValueError as ve:
            print(f"Error with inputs '{t1}' and '{t2}': {ve}")

    # Additional explicit test for error handling
    try:
        time_difference_seconds("invalid", "08:15:30")
    except ValueError as e:
        print(f"\nExpected error caught correctly: {e}")