import re

def parse_time_string(time_str: str) -> int:
    """
    Parses a time difference string into total minutes.
    
    Supports formats like:
        - "2 hours 30 minutes"
        - "1 hour 45 mins" (singular/plural variations handled via regex groups)
        - "90 minutes", "60 min", etc.
        
    Args:
        time_str (str): A string representing a duration with 'hours' and/or 'minutes'.
        
    Returns:
        int: Total elapsed time in minutes.
        
    Raises:
        ValueError: If the input format is not recognized or contains invalid data.
    """
    
    # Pattern to match hours, optional separator (space), and minutes
    pattern = r'(\d+)\s*(?:hours?|hrs?)?\s*([\d.,]+)\s*(?:minutes?|mins?)?'
    
    matches = re.findall(pattern, time_str.lower())
    
    if not matches:
        raise ValueError(f"Unable to parse time string: '{time_str}'")
    
    total_minutes = 0
    
    for match in matches:
        hours_part, minutes_part = map(float, match)
        
        # Handle cases where only one part is present (e.g., "90 minutes")
        if not hours_part and not minutes_part:
            continue
            
        if hours_part > 0 or minutes_part > 0:
            total_hours = int(hours_part)
            
            try:
                total_minutes += float(minutes_part) * 60 + (total_hours * 60)
            except ValueError:
                raise ValueError(f"Invalid numeric value in time string: '{time_str}'")
    
    return round(total_minutes)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    
    test_cases = [
        "2 hours 30 minutes",
        "1 hour 45 mins",
        "90 minutes",
        "60 min",
        "3 hrs 15 minutes",
        "0.5 hours 30 minutes", # Edge case with decimal hours
    ]
    
    print("Parsing time differences and calculating total minutes:\n")
    
    for test_input in test_cases:
        try:
            result = parse_time_string(test_input)
            print(f"Input: '{test_input}' -> {result} minute(s)")
        except ValueError as e:
            print(f"Error parsing '{test_input}': {e}")