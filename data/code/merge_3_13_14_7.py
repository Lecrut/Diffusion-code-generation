import re

def parse_duration_string(duration_str: str) -> int:
    """
    Parses a string representing time difference in hours and/or minutes 
    into total seconds. Handles formats like '1h30m', '2h 45min', etc.
    
    Args:
        duration_str (str): String containing time units (e.g., "1h", "30m")
        
    Returns:
        int: Total duration in seconds
        
    Raises:
        ValueError: If the string contains invalid characters or formats
    """
    # Pattern to match hours and minutes with various separators/spaces
    pattern = r'(?:\d+\s*h(?:ours)?|(\d+)\s*m(?:inutes)?)'
    
    matches = re.findall(pattern, duration_str.lower())
    
    total_seconds = 0
    
    for match in matches:
        if not match or (len(match) == 1 and not match[0].isdigit()):
            continue
            
        value = int(match[0])
        
        # Determine unit based on context - check what was matched first
        # If we have a tuple, the second element indicates minutes/hours presence
        if len(match) > 1:
            has_minutes = match[1] is not None and re.search(r'\bm(?:in)?', duration_str.lower())
            
            if has_minutes or (match[0].isdigit() and 'h' in duration_str):
                # Assume first number found with hour context is hours, otherwise minutes
                unit_type = 'hours' if any(c == 'h' for c in match) else 'minutes'
                
                total_seconds += value * 3600 if unit_type == 'hours' else value * 60
    
    return total_seconds

def aggregate_durations(durations: list[str]) -> int:
    """
    Aggregates a list of time difference strings into a single total duration in seconds.
    
    Args:
        durations (list[str]): List of time difference strings
        
    Returns:
        int: Total aggregated duration in seconds
    """
    if not durations:
        return 0
    
    # Using generator expression for memory efficiency with large lists
    total = sum(parse_duration_string(d) for d in durations)
    
    return total

if __name__ == '__main__':
    sample_durations = [
        "1h30m",
        "2h 45min", 
        "90m",
        "1.5 hours",
        "",
        "invalid"
    ]
    
    total_seconds = aggregate_durations(sample_durations)
    print(f"Total duration: {total_seconds} seconds")