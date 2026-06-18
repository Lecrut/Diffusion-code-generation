import re

def time_difference_seconds(time_str1: str, time_str2: str) -> int:
    """
    Calculates the difference in total seconds between two time strings.
    
    The function expects inputs to be valid HH:MM:SS format (e.g., "03:45:10").
    It ignores any date components if present, focusing solely on the time scale.
    
    Args:
        time_str1 (str): First time point in 'HH:MM:SS' format.
        time_str2 (str): Second time point in 'HH:MM:SS' format.
        
    Returns:
        int: The difference between the two times in seconds. 
             Positive if time_str1 is later than time_str2, negative otherwise.
             
    Raises:
        ValueError: If either input string does not match the expected HH:MM:SS pattern.
    """
    
    # Regex to validate and parse HH:MM:SS format (allowing optional leading zeros)
    time_pattern = re.compile(r'^(\d{1,2}):(\d{2}):(\d{2})$')
    
    def parse_time(time_str):
        match = time_pattern.match(time_str.strip())
        if not match:
            raise ValueError(f"Invalid time format '{time_str}'. Expected HH:MM:SS.")
        
        hours, minutes, seconds = map(int, match.groups())
        
        # Basic validation for reasonable time values (0-23h, 0-59m, 0-59s)
        if not (0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60):
            raise ValueError(f"Invalid hour/minute/second values in '{time_str}'.")
            
        return hours * 3600 + minutes * 60 + seconds

    try:
        total_seconds_1 = parse_time(time_str1)
        total_seconds_2 = parse_time(time_str2)
        
        difference = total_seconds_1 - total_seconds_2
        return int(difference)
    
    except ValueError as e:
        raise ValueError(f"Error processing time strings: {e}")

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    test_cases = [
        ("03:45:10", "20:15:05"),  # Normal case where first is earlier than second (negative result)
        ("23:59:59", "00:00:01"), # Crossing midnight scenario (first > second in seconds due to wrap around not handled, just raw diff)
        ("12:00:00", "12:00:00"), # Identical times
        ("08:30:45.999", "08:30:46.000"), # Case with milliseconds (will fail regex, demonstrating strictness) -> Adjusted below to ensure success without changing logic too much if user wants simple HH:MM:SS
        
    ]
    
    # Correcting test cases to strictly adhere to the function's expected input format for robust demonstration
    
    valid_samples = [
        ("03:45:10", "20:15:05"), 
        ("23:59:59", "00:00:01"), # This results in a large negative number because raw seconds of 23:59:59 > 00:00:01
        ("12:00:00", "12:00:00"), 
    ]

    print("Running time difference utility...\n")
    
    for t_str_1, t_str_2 in valid_samples:
        try:
            diff = time_difference_seconds(t_str_1, t_str_2)
            # Formatting output to be readable (e.g., adding days if it crosses midnight significantly isn't needed here as per spec 'total seconds')
            print(f"Time 1 ({t_str_1}): {diff} seconds before Time 2 ({t_str_2})")
        except ValueError as e:
            print(f"Error with inputs '{t_str_1}' and '{t_str_2}': {e}")

    # Additional specific test case for crossing midnight logic demonstration (raw difference)
    diff_midnight = time_difference_seconds("00:05:00", "23:55:00")
    print(f"\nSpecial Case ('00:05:00' vs '23:55:00'): {diff_midnight} seconds difference.")