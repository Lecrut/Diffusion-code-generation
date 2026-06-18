import re

def parse_time_string(time_str: str) -> int:
    """
    Parses a time difference string into total minutes.
    
    Supports formats like:
        "2 hours 30 minutes"
        "1 hour", "45 mins" (case-insensitive, flexible spacing)
        
    Returns the equivalent value in minutes as an integer.
    Raises ValueError if parsing fails due to unsupported format or invalid tokens.
    """
    
    # Normalize whitespace and convert to lowercase for consistent matching
    normalized = time_str.strip().lower()
    
    # Define regex patterns for flexible token extraction
    hours_pattern = r'\s*(\d+)\s*hours?\b'
    minutes_pattern = r'\s*(\d+)\s*(minutes?|mins?)\b'
    
    matches = {}
    
    hour_match = re.search(hours_pattern, normalized)
    minute_match = re.search(minutes_pattern, normalized)
    
    if not hour_match and not minute_match:
        raise ValueError(f"Unable to parse time string: '{time_str}'")
        
    hours_val = int(hour_match.group(1)) if hour_match else 0
    
    # Handle singular/plural forms for minutes (mins/minutes/mintues)
    min_matches = re.findall(r'(\d+)\s*(?:minute|min)?\b', normalized, flags=re.IGNORECASE)
    
    total_minutes_sum = hours_val * 60
    if not minute_match:
        raise ValueError(f"Unable to parse time string: '{time_str}'")

    for min_group in re.finditer(r'(\d+)\s*(?:minute|min)?\b', normalized):
            val = int(min_group.group(1))

if __name__ == '__main__':
    pass
