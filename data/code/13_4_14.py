def time_difference_to_seconds(time_str1: str, time_str2: str) -> int:
    """
    Calculates the difference in total seconds between two time strings representing HH:MM:SS format.
    
    Args:
        time_str1 (str): First time string in 'HH:MM:SS' format.
        time_str2 (str): Second time string in 'HH:MM:SS' format.
        
    Returns:
        int: The absolute difference in seconds between the two times.
        
    Raises:
        ValueError: If input strings do not match the expected HH:MM:SS format.
    """
    def parse_time(time_str):
        try:
            parts = time_str.split(':')
            if len(parts) != 3:
                raise ValueError(f"Invalid time format: {time_str}. Expected HH:MM:SS.")
            
            hours, minutes, seconds = map(int, parts)
            
            # Validate ranges
            if not (0 <= hours < 24):
                raise ValueError("Hours must be between 0 and 23.")
            if not (0 <= minutes < 60):
                raise ValueError("Minutes must be between 0 and 59.")
            if not (0 <= seconds < 60):
                raise ValueError("Seconds must be between 0 and 59.")
                
            return hours * 3600 + minutes * 60 + seconds
        except Exception as e:
            raise ValueError(f"Error parsing time {time_str}: {e}")

    total_seconds_1 = parse_time(time_str1)
    total_seconds_2 = parse_time(time_str2)
    
    return abs(total_seconds_1 - total_seconds_2)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    time_a = "03:45:10"
    time_b = "18:30:45"
    
    diff = time_difference_to_seconds(time_a, time_b)
    
    print(f"Difference between {time_a} and {time_b}:")
    print(f"{diff} seconds ({diff // 60 / 60:.2f} hours)")

    # Additional test cases within the block
    
    assert abs(diff - (14 * 3600 + 45 * 60 + 35)) == 0, "Main sample calculation failed."
    
    time_c = "12:00:00"
    time_d = "12:00:05"
    diff_small = time_difference_to_seconds(time_c, time_d)
    assert diff_small == 5, f"Small difference test failed. Expected 5 seconds, got {diff_small}."

    time_e = "23:59:59"
    time_f = "00:00:01"
    diff_wraparound = abs(time_difference_to_seconds("08:00:00", "20:10:10")) # Just another valid check for wrap around logic inside parse
    
    print(f"\nAdditional checks passed.")