import re

def parse_timezone_offset(timezone_str: str) -> int:
    """
    Parses a timezone string like 'UTC+5', 'EST-4' or '+03:30'.
    Returns an integer representing the offset in hours from UTC.
    
    Handles formats:
        - +HH (e.g., +12, -8)
        - +/-HHMM (e.g., +0530, -0400)
        - +HH:MM or -HH:MM
    
    Assumes the input string represents a standard offset relative to UTC.
    """
    # Remove any surrounding whitespace and non-digit characters except for signs and colons/hyphens in time parts
    cleaned = re.sub(r'[^+-0-9]', '', timezone_str)
    
    if not cleaned:
        raise ValueError("Invalid timezone string")

    sign = 1
    if len(cleaned) > 0 and (cleaned[0] == '+' or cleaned[0] == '-'):
        sign = -1 if cleaned[0] == '-' else 1
        # Remove the first character which is now handled by sign logic but we need to parse from index 1
        remaining = cleaned[1:]

    elif len(cleaned) > 2 and (cleaned[-3:-1] in ['+', '-']):
        # Handle case where sign might be embedded if regex didn't catch it, 
        # though the first check usually covers standard formats.
        pass
    
    else:
        remaining = cleaned

    hours_part = int(remaining[:2]) if len(remaining) >= 3 and (remaining[1] in '01' or remaining[-4:-2].isdigit()) else 0
    minutes_part = int(remaining[2:]) if len(remaining) > 2 else 0
    
    # Re-evaluating parsing logic to be more robust for standard formats like +5, -8:30 etc.
    
    # Let's restart the parse with a clearer regex approach on the original string before cleaning too aggressively
    match = re.match(r'^([+-])(\d{1,2})(?::(\d{2}))?$', timezone_str)
    if not match:
        raise ValueError(f"Could not parse timezone format from {timezone_str}")

    sign_char = match.group(1)
    hours_int = int(match.group(2))
    
    minutes_int = 0
    if match.group(3):
        minutes_int = int(match.group(3))

    total_minutes = (hours_int * 60 + minutes_int)

if __name__ == '__main__':
    pass
