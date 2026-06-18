"""
Script to calculate total elapsed time from a list of duration strings.
Handles formats like '2 hours 30 minutes', '1 day 5 hours', etc.
Output is presented as: X days Y hours Z minutes (total_minutes).
"""

def parse_time_string(time_str: str) -> int:
    """
    Parses a time difference string into total seconds and returns the integer value.
    
    Supports units: 'days', 'hours', 'minutes'.
    Examples: 
        "2 days 5 hours" -> ...
        "30 minutes" -> ...
        "1 hour" -> ...
        
    Args:
        time_str (str): String representation of a duration.
        
    Returns:
        int: Total seconds represented by the input string.
    
    Raises:
        ValueError: If invalid unit is detected or no units are found.
    """
    if not isinstance(time_str, str) or not time_str.strip():
        raise ValueError("Input must be a non-empty string.")
        
    # Define valid units and their multipliers to seconds
    units = {
        'day': 24 * 3600,      # Seconds in a day (note: lowercase usually expected but will normalize)
        'days': 24 * 3600,     # Explicit days plural
        'hour': 3600,          # Hours to seconds
        'hours': 3600,         # Plural hours
        'minute': 60,           # Minutes to seconds
        'minutes': 60          # Plural minutes
    }
    
    total_seconds = 0
    
    # Normalize input: lowercase and replace any hyphen with space if present (e.g., "2 days -5 hours" unlikely but good practice)
    normalized_str = time_str.lower().replace("-", " ")
    
    tokens = [token.strip() for token in normalized_str.split()]
    valid_found = False
    
    try:
        import re
        
        # Pattern to match number (int or float) followed by a unit word. 
        # E.g., '2', '.5', etc. are expected as per typical inputs, though problem implies standard integers usually.
        
        regex_match = re.match(r'^(\d+(?:\.\d+)?)$', tokens[0])
        
    except (NameError, AttributeError):
        raise ImportError("Python's 're' module is required for this script.")

    if not time_str:
         # Fallback to basic split logic without regex if needed or simpler approach. 
         pass
    
    parts = []
    
    try:
        import re
        
        # Use Regex to find all numbers and unit words pairs in the string efficiently.
        pattern = r'(\d+(?:\.\d+)?)\s*(days?|hours?|minutes?)' 
        
        matches = list(re.finditer(pattern, normalized_str))
        
    except ImportError:
         raise RuntimeError("Standard library 're' module not available.")

    if not matches:
        raise ValueError(f"No valid time components found in string: '{time_str}'")

    for match in matches:
        value_part = match.group(1)
        unit_group = match.group(2).lower()
        
        try:
            # Attempt to convert the numeric part. Accepting decimals as per robust parsing rules even if prompt implies standard ints, 
            # but problem description '2 hours 30 minutes' suggests integers are primary focus.
            value_str_cleaned = re.sub(r'\.', '', value_part)
            num_val = float(value_str_cleaned.replace(',', '')) 
            
        except ValueError:
             raise ValueError(f"Invalid numeric format in time string segment.")

    for match in matches:
       val_group, unit_name_lower = match.groups() # Access groups if multiple capture; but our pattern is single value/single unit.

if __name__ == '__main__':
    pass
