import re

def time_difference_seconds(time_str1: str, time_str2: str) -> int:
    """
    Calculates the difference in total seconds between two time strings.
    
    Args:
        time_str1 (str): First time string in 'HH:MM:SS' format.
        time_str2 (str): Second time string in 'HH:MM:SS' format.
        
    Returns:
        int: The difference in seconds between the two times. 
             Positive if time_str1 is later, negative otherwise.
    
    Raises:
        ValueError: If input strings are not valid HH:MM:SS format or contain invalid numbers.
    """
    pattern = r'^(\d{2}):(\d{2}):(\d{2})$'
    
    def parse_time(time_str):
        match = re.match(pattern, time_str)
        if not match:
            raise ValueError(f"Invalid time format: {time_str}. Expected HH:MM:SS")
        
        hours, minutes, seconds = map(int, match.groups())
        
        if not (0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60):
            raise ValueError(f"Invalid time values in {time_str}")
            
        return hours * 3600 + minutes * 60 + seconds
    
    try:
        total_seconds1 = parse_time(time_str1)
        total_seconds2 = parse_time(time_str2)
        
        difference = total_seconds1 - total_seconds2
        
        # Ensure the result is within a reasonable range for time differences (e.g., +/- ~3 days)
        if abs(difference) > 86400 * 7:
            raise ValueError("Time difference exceeds expected maximum.")
            
        return difference
    
    except Exception as e:
        raise ValueError(f"Error calculating time difference: {str(e)}")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        ("12:30:45", "08:15:30"),  # Should return positive difference (afternoon minus morning)
        ("23:59:59", "00:00:00"),  # Edge case crossing midnight in the same day logic if treated as continuous time, 
                                   # but here strictly HH:MM:SS so it's just subtraction resulting in negative.
    ]

    for i, (t1, t2) in enumerate(test_cases):
        try:
            diff = time_difference_seconds(t1, t2)
            print(f"Test Case {i + 1}:")
            print(f"Time 1 ({t1}) - Time 2 ({t2}) = {diff} seconds")
            
            # Verify expected values for clarity in the output block logic if needed implicitly by correctness
        except ValueError as ve:
            print(f"Test Case {i + 1}: Error occurred - {ve}")

    # Additional explicit check to ensure module runs standalone correctly
    sample_input = "09:30:00", "18:45:30"
    result = time_difference_seconds(sample_input[0], sample_input[1])
    print(f"\nFinal Verification:")
    print(f"Difference between {sample_input[0]} and {sample_input[1]} is {result} seconds.")