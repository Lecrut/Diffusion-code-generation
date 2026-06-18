def format_duration(duration_string: str) -> str:
    """
    Converts a time duration string in 'HH:MM:SS' format 
    into a human-readable string 'Days, Hours, Minutes, Seconds'.
    
    Args:
        duration_string (str): Time duration in 'HH:MM:SS' format.
        
    Returns:
        str: Human-readable formatted string with leading zeros for single-digit values.
             If the total seconds exceed 24 hours, it includes days; otherwise just H:M:S.
    """
    try:
        parts = duration_string.split(':')
        if len(parts) != 3:
            raise ValueError("Invalid format: expected 'HH:MM:SS'")

        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = int(parts[2])

        total_seconds = (hours * 3600) + (minutes * 60) + seconds
        
        days = total_seconds // (86400)
        remaining_after_days = total_seconds % 86400
        hours_in_output = remaining_after_days // 3600
        minutes_in_output = (remaining_after_days % 3600) // 60
        seconds_in_output = remaining_after_days % 60

        if days > 0:
            return f"{days} Days, {hours_in_output:02d} Hours, {minutes_in_output:02d} Minutes, {seconds_in_output:02d} Seconds"
        else:
            return f"{hours_in_output:02d} Hours, {minutes_in_output:02d} Minutes, {seconds_in_output:02d} Seconds"

    except ValueError as e:
        raise ValueError(f"Invalid input format or values: {e}")

if __name__ == '__main__':
    # Hard-coded sample inputs to test the function without user interaction
    samples = [
        "1:30:45",      # Less than 2 hours, no days
        "24:00:00",     # Exactly one day
        "25:01:00",     # More than one day
        "0:0:0"         # Zero duration
    ]

    for sample in samples:
        result = format_duration(sample)
        print(f"{sample} -> {result}")