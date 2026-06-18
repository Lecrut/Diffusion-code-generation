import re

def parse_time_to_minutes(time_str: str) -> int:
    """
    Converts a time string like '2 hours 30 minutes' or '15 min' into total minutes.
    
    Supports formats such as:
        - X hours Y minutes (e.g., "2 hours 30 minutes")
        - X hour(s) y minute(s) with singular/plural variations
        - Just hours, just minutes, etc.
        
    Args:
        time_str (str): String representing a duration in words and numbers.
        
    Returns:
        int: Total elapsed time in minutes.
        
    Raises:
        ValueError: If the string cannot be parsed into valid numeric components for time units.
    """
    
    # Define regex patterns to extract number + unit combinations
    # Matches optional digits followed by 'hours', 'hour' or 'minutes', 'minute' (case-insensitive)
    pattern = re.compile(r'(?:\d+)\s*(?:(?:hours|hour)|(?:minutes|min))?\b')
    
    matches = list(pattern.finditer(time_str.lower()))
    
    total_minutes = 0
    
    for match in sorted(matches, key=lambda m: -m.start()):
        value_str = match.group(1) if len(match.groups()) > 0 else "1" # Default to 1 if no number found (though regex usually requires it)
        
        try:
            num = int(value_str)
        except ValueError as e:
            raise ValueError(f"Invalid numeric value '{value_str}' in time string") from e
            
        unit = match.group(2).lower() # The full matched word like 'hours', 'minutes' etc. or None if pattern didn't catch the whole thing nicely but we need to be careful
        
        # Better approach: explicitly map found units
        extracted_units = {}
        
    # Re-implementation with a more robust extraction strategy
    
    time_str_cleaned = time_str.lower().strip()
    
    total_minutes = 0
    
    # Extract all occurrences of number followed by 'hours' or 'minutes' (singular/plural variations)
    hour_matcher = re.compile(r'\d+\s*(?:hour|hours)\b', flags=re.IGNORECASE)
    min_matcher = re.compile(r'\d+\s*(?:minute|min(?:utes))\b', flags=re.IGNORECASE) # Note: 'mins' is often used but let's stick to standard "minutes" or "min" if needed. Let's handle "minutes", "min".
    
    # Actually, the prompt examples are like '2 hours 30 minutes'. 
    # We should support singular/plural and potentially abbreviations if common, but strict adherence to example is safer first.
    # Let's refine regexes for specific unit words found in examples or similar natural language formats.
    
    hour_regex = re.compile(r'(\d+)\s*hour(s)?', flags=re.IGNORECASE)
    minute_regex = re.compile(r'(\d+)\s*(?:minute|minutes|min)', flags=re.IGNORECASE) # Support 'min' as abbreviation for min
    
    all_matches_hour, all_matches_min = [], []
    
    found_units = set()
    
    while True:
        h_match = hour_regex.search(time_str_cleaned)
        m_match = minute_regex.search(time_str_cleaned)
        
        if not h_match and not m_match:
            break

if __name__ == '__main__':
    pass
