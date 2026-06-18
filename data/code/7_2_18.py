def parse_duration_to_seconds(time_string: str) -> int:
    """
    Converts a time string in 'H:M:S' format to total seconds.
    
    Args:
        time_string (str): A string representing hours, minutes, and seconds separated by colons.
        
    Returns:
        int: Total duration in seconds.
        
    Raises:
        ValueError: If the input string is not in 'H:M:S' format or contains invalid numbers.
    """
    
    # Split the time string into parts based on the colon delimiter
    try:
        hours, minutes, seconds = map(int, time_string.split(':'))
        
        # Calculate total seconds from individual components
        return (hours * 3600) + (minutes * 60) + seconds
        
    except ValueError as ve:
        raise ValueError(f"Invalid input format '{time_string}'. Expected 'H:M:S' with numeric values.")

def main():
    """
    Main function to demonstrate the duration converter.
    
    This block contains hard-coded sample inputs and processes them,
    printing the calculated total seconds for each case without any user interaction.
    """
    
    # Hard-coded sample time strings in 'H:M:S' format
    sample_inputs = [
        "1:30:45",   # 1 hour, 30 minutes, 45 seconds
        "2:45:30",   # 2 hours, 45 minutes, 30 seconds
        "0:15:00",   # 15 minutes only (0 hours)
    ]
    
    print("Duration Conversion Results:")
    for time_str in sample_inputs:
        total_seconds = parse_duration_to_seconds(time_str)
        formatted_time = f"{time_str} ({'H:M:S'})"
        result_msg = f"{formatted_time} -> {total_seconds} seconds"
        print(result_msg)

if __name__ == '__main__':
    main()