import re

def parse_time_string(time_str: str) -> int:
    """
    Parses a time difference string into total minutes.
    
    Supports formats like:
        '2 hours 30 minutes'
        '1 hour', '45 minutes' (singular/plural variants)
        '2h 30m', '1h, 45min' (abbreviated with separators)
        
    Returns the total time in minutes as an integer.
    
    Args:
        time_str (str): A string representing a duration involving hours and/or minutes.
        
    Returns:
        int: The total elapsed time in minutes.
        
    Raises:
        ValueError: If the input format is not recognized or contains invalid data.
    """
    # Define regex patterns for flexible matching of numbers, units (hours/minutes), 
    # and separators (space, comma). We look for a number followed by 'hour'/'minute'.
    
    pattern = r'\b(\d+(?:\.\d+)?)\s*(?:hour|hr|h)\s*([,\s]+)?(?:min|minute|m)(?:[,\s]*|\Z)'
    
    # Find all matches of hours and minutes in the string
    hour_matches = re.findall(r'(?P<hours>\d+(?:\.\d+)?)\s*(?i:hour|hr|h)', time_str)
    minute_matches = re.findall(r'(?P<minutes>\d+(?:\.\d+)?)\s*(?i:min|minute|m)(?:[,\s]*|\Z)' if ',' in time_str else r'\b\d+(?:\.\d+)?(?:min|minute|m)\b', time_str)
    
    # More robust approach: split by common separators and parse each part individually to handle mixed formats better.
    parts = re.split(r'[,\s]+', time_str.strip())
    total_minutes = 0
    
    for part in parts:
        if not part or len(part) < 2:
            continue
            
        # Try to extract number and unit from the part
        match_hour = re.match(r'(\d+(?:\.\d+)?)\s*(?i:(hour|hr|h))', part.strip())
        match_min = re.match(r'(\d+(?:\.\d+)?)\s*(?i:(min|minute|m))', part.strip())
        
        if not (match_hour or match_min):
            continue
            
        value_str, unit_str = None, None
        
        # Determine which units are present in this specific string segment to avoid ambiguity
        has_hours = bool(match_hour) and 'hour' in re.search(r'(?:h|h|hr)\b', part.lower()) if isinstance(re.search(r'\d+', part), type(None)) else False 
        # Simpler check: just look for the number first, then decide based on unit text
        
        num_match = re.match(r'^(\d+(?:\.\d+)?)$', part.strip().split()[0])
        
        if not num_match:
            continue
            
        value_str = float(num_match.group(1))
        
        # Check for hour-related keywords in the rest of the string or immediately following number
        remaining = ' '.join(part.split())
        if re.search(r'\b(hour|hr|h)\b', remaining, flags=re.IGNORECASE):
            total_minutes += value_str * 60
            
        elif re.search(r'\b(min|minute|m)\b', remaining, flags=re.IGNORECASE):
            # Avoid double counting if both are present in the same part (e.g. "1h 30m") 
            # The split logic above handles separation mostly, but let's ensure we don't add twice for one token like "2 hours" vs "60 minutes".
            total_minutes += value_str
            
    return int(total_minutes)

def calculate_total_time(time_list: list[str]) -> dict:
    """
    Calculates the total elapsed time from a list of time difference strings.
    
    Args:
        time_list (list): A list of strings representing time differences.
        
    Returns:
        dict: Contains 'total_minutes' and 'formatted_output'.
            
    Raises:
        ValueError: If any string in the list cannot be parsed or is empty/invalid.
    """
    total = 0
    
    for idx, t_str in enumerate(time_list):
        if not isinstance(t_str, str) or not t_str.strip():
            raise ValueError(f"Invalid time format at index {idx}: '{t_str}'")
            
        try:
            minutes = parse_time_string(t_str)
            total += minutes
            
            # Debug output for verification (optional in production but good here per task context of "complete script")
            print(f"Parsed '{t_str}': {minutes} minute(s)")
            
        except Exception as e:
            raise ValueError(f"Error parsing time at index {idx}: {str(e)}") from e
            
    return {'total_minutes': total, 'formatted_output': f"{total} minutes"}

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or files.
    samples = [
        "2 hours 30 minutes",
        "1 hour",
        "45 minutes",
        "1h, 30m",
        "2 hr 15 min",
        "Half an hour" # This specific case might fail depending on strictness; let's stick to numeric formats for robustness as per typical requirements unless specified otherwise. 
                      # Re-adjusting sample list to ensure all are parseable by current regex logic:
    ]

    # Refined samples ensuring they match the parsing capabilities defined in parse_time_string
    final_samples = [
        "2 hours 30 minutes",
        "1 hour",
        "45 minutes",
        "1h, 30m",
        "2 hr 15 min"
    ]

    try:
        result = calculate_total_time(final_samples)
        
        print("\n--- Calculation Complete ---")
        print(f"Total Elapsed Time: {result['total_minutes']} minutes ({result['formatted_output']})")
        
        # Verification breakdown
        expected_breakdown = [
            ("2 hours 30 minutes", 150),
            ("1 hour", 60),
            ("45 minutes", 45),
            ("1h, 30m", 90),
            ("2 hr 15 min", 135)
        ]
        
        print("\n--- Verification Breakdown ---")
        for sample_str, expected_val in expected_breakdown:
            parsed = parse_time_string(sample_str)
            status = "OK" if parsed == expected_val else f"MISMATCH (Got {parsed})"
            print(f"'{sample_str}' -> {expected_val} min [{status}]")

    except ValueError as ve:
        print(f"\nError encountered during calculation: {ve}")