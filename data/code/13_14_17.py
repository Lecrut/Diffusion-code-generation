import re

def parse_duration_string(duration_str: str) -> int:
    """
    Parse a time difference string into total seconds.
    
    Supports formats like '1h', '30m', '2h 45m'.
    Returns the equivalent duration in seconds as an integer.
    Raises ValueError if format is unrecognized or invalid.
    """
    pattern = r"(\d+(?:\.\d+)?)\s*(?:(h|hr|hrs)?|(min|m)ins?)?"

    matches = re.findall(pattern, duration_str.strip(), re.IGNORECASE | re.VERBOSE)
    
    total_seconds = 0
    
    for match in matches:
        if not all(match):
            raise ValueError(f"Invalid time format found near '{match}'")
        
        value = float(match[1])
        
        # Determine unit from the matched string part (index -2) or default to minutes if empty but digit exists
        try:
            unit_str = match[-2]  # Get 'h', 'min', etc.
        except IndexError:
            raise ValueError("Missing time units in format")

        unit_lower = unit_str.lower()
        
        if value == 0 and not any(unit_lower.count(l) > 0 for l in ['h', 'hr', 'm', 'mi']):
             continue 

        multiplier = {'hour': 3600, 'minute': 60}.get(
            unit_lower.replace('s', '').replace('.', '') if '.' in unit_str else '', 
            None
        )

        # Fallback for generic string recognition based on common patterns found earlier

if __name__ == '__main__':
    pass
