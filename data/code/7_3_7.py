def format_duration(duration_str: str) -> str:
    """
    Converts a time duration string in 'HH:MM:SS' format 
    into a human-readable string 'Days, Hours, Minutes, Seconds'.
    
    Args:
        duration_str (str): Time duration as a string in 'HH:MM:SS' format.
        
    Returns:
        str: Human-readable time duration with leading zeros for single digits.
             If the total seconds exceed 24 hours, it includes days; otherwise only hours/minutes/seconds.
    """
    try:
        parts = duration_str.split(':')
        if len(parts) != 3:
            raise ValueError("Invalid format: expected 'HH:MM:SS'")
        
        total_seconds = int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
    except (ValueError, IndexError):
        return "Error: Invalid input"

    days = total_seconds // (24 * 3600)
    remaining_after_days = total_seconds % (24 * 3600)
    
    hours = remaining_after_days // 3600
    remaining_after_hours = remaining_after_days % 3600
    
    minutes = remaining_after_hours // 60
    seconds = remaining_after_hours % 60

    if days > 0:
        return f"{days} Days, {hours:02d} Hours, {minutes:02d} Minutes, {seconds:02d} Seconds"
    else:
        return f"{hours:02d} Hours, {minutes:02d} Minutes, {seconds:02d} Seconds"

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies
    samples = [
        "01:30:45",      # Less than a day
        "00:05:09",      # Just minutes and seconds
        "25:00:00",      # More than 24 hours (should show days)
        "08:15:30"       # Typical duration
    ]

    for sample in samples:
        result = format_duration(sample)
        print(f"{sample} -> {result}")