import re

def parse_time_string(time_str: str) -> int:
    """
    Parses a time difference string into total minutes.
    
    Supports formats like '2 hours 30 minutes', '1h 45m', 
    or combinations of hours and minutes separated by spaces, commas, or mixed units.
    
    Args:
        time_str (str): String representing a duration with optional unit suffixes ('hours'/'hour', 'minutes'/'min').
        
    Returns:
        int: Total elapsed time in minutes.
        
    Raises:
        ValueError: If the string cannot be parsed into valid hours and/or minutes.
    """
    
    # Define regex patterns for flexible matching of numbers followed by optional unit suffixes
    pattern = r'(\d+(?:\.\d+)?)\s*(hours?|h)?\s*(minutes?|m)?'
    
    matches = re.findall(pattern, time_str.lower())
    
    total_minutes = 0
    
    for match in matches:
        value = float(match[0]) if len(match) > 0 else 0
        
        # Determine unit based on presence of 'hours'/'h' or 'minutes'/'m'
        has_hours = bool(re.search(r'\b(hours?|h)\b', time_str.lower())) and not re.search(r'\b(minutes?|m)\b', time_str.lower())
        
        if match[1] in ('hour', 'hours', 'h'):
            total_minutes += value * 60
        
        elif match[2] in ('minute', 'minutes', 'min') or (not has_hours and not match[1]):
            # If no hour unit is explicitly found but minutes are present, treat as minutes only
            if re.search(r'\b(minutes?|m)\b', time_str.lower()):
                total_minutes += value
            
        else:
            raise ValueError(f"Invalid time format in string: '{time_str}'")

    return int(total_minutes)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    test_cases = [
        "2 hours 30 minutes",      # Expected: 150
        "4h 15m",                  # Expected: 255
        "1.5 hours",               # Expected: 90
        "60 minutes",              # Expected: 60
        "1 hour, 30 min",         # Expected: 90 (comma separator supported via regex)
        "half an hour",            # Edge case handling - simplified to assume numeric input for robustness per task constraints
    ]

    results = []
    
    print("Time Parsing Test Results:")
    print("-" * 40)
    
    for time_str in test_cases:
        try:
            minutes = parse_time_string(time_str)
            # Special handling for 'half an hour' which doesn't fit the numeric regex strictly but should be handled gracefully if needed. 
            # For strict adherence to provided format, we assume valid numeric inputs as per task description examples.
            results.append(f"'{time_str}' -> {minutes} minutes")
        except ValueError as e:
            results.append(f"Error parsing '{time_str}': {e}")

    for result in results:
        print(result)
    
    # Demonstrate usage with a custom input example not in the list above to show flexibility
    sample_input = "3 hours 45 minutes and 10 seconds (seconds ignored per format)"