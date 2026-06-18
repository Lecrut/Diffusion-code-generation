import re
from typing import List, Union

def parse_duration_string(duration_str: str) -> int:
    """
    Parses a string representing time difference in hours and/or minutes 
    into total seconds. Handles optional negative signs and spaces around operators.
    
    Args:
        duration_str (str): String like "1h 30m", "-2h 45m", etc.
        
    Returns:
        int: Total duration in seconds
        
    Raises:
        ValueError: If the string format is invalid or contains unsupported units.
    """
    pattern = r'(-?\d+)\s*(?:hours?|hrs?)\s*([+-])\s*(-?\d+)(?:m(?:inutes?|ins)?)?'
    
    match = re.match(pattern, duration_str.strip(), re.IGNORECASE | re.DOTALL)
    if not match:
        raise ValueError(f"Invalid time format: {duration_str}")

    hours_val = int(match.group(1))
    sign_char = match.group(2).strip()
    minutes_val = 0
    
    # Check for additional minute component with explicit operator (e.g., "h + m")
    if len(duration_str) > re.match(r'^-?\d+\s*(?:hours?|hrs?)\s*[+-]\s*-?\d+', duration_str, re.IGNORECASE).end():
        full_match = re.search(pattern, duration_str.strip())
        hours_val = int(full_match.group(1)) if full_match else 0
        
    # Re-evaluate with a more robust approach for mixed units like "h + m" or "-2h -3m"
    
    parts = []
    current_part = ""
    prev_sign = '+'
    
    tokens = duration_str.replace(' ', '').replace(',', '')
    if not re.match(r'^-?\d+[hmH]+$', tokens):
        # Handle explicit operators like "1h + 30m" or "-2h -45m"
        operator_pattern = r'(-?\d+)([hH][mm]?)|([+-])\s*(-?\d+)([hH][mm]?)'
        
    # Simpler robust parsing: split by operators and numbers, then reconstruct
    
    tokens_list = re.findall(r'-?\d+[hmHM]', duration_str) + [x for x in ['+', '-'] if '+' not in duration_str or '-' not in duration_str]
    
    # Actually, let's just parse the whole string linearly to be safe against "1h+30m" vs "1 h 30 m"
    
    total_seconds = 0
    
    # Find all number-unit pairs and their signs based on position or explicit operators
    matches = re.finditer(r'(-?\d+)\s*(?:hours?|hrs?)\s*([+-])?', duration_str)
    
    for match in matches:
        val = int(match.group(1))
        unit_type = 'h' if ('hour' in match.group(0).lower() or 'hr' in match.group(0).lower()) else 'm'
        
        # Determine sign based on explicit operator following the number, 
        # but only if there's a gap (e.g. "1h + 30m") vs concatenated ("1h+30m" might be ambiguous)
        # The regex above captures an optional sign after the unit name
        
    # Let's restart with a definitive parsing strategy for mixed units like "2h -45m" or "-2h 30m"
    
    def parse_time_part(part: str):
        """Parses a single part like '1h', '-2 hours', etc."""
        match = re.match(r'^(-?\d+)\s*(?:hours?|hrs?)\s*([+-])?', part.strip())
        if not match:
            raise ValueError(f"Cannot parse time unit: {part}")
        
        value = int(match.group(1))
        sign_char = match.group(2) or '+' # Default to positive
        
        return value * (1 if sign_char == '+' else -1), 'h'

    def parse_time_part_m(part: str):
        """Parses a single part like '30m', '-45 minutes'"."""
        match = re.match(r'^(-?\d+)\s*(?:minutes?|mins|m(?:in)?)\s*([+-])?', part.strip())
        if not match:
            raise ValueError(f"Cannot parse time unit: {part}")
        
        value = int(match.group(1))
        sign_char = match.group(2) or '+' # Default to positive
        
        return value * (1 if sign_char == '+' else -1), 'm'

    total_seconds = 0
    
    # Split by explicit operators first, then process each chunk
    chunks = re.split(r'\s*[+-]\s*', duration_str.strip())
    
    for chunk in chunks:
        cleaned_chunk = chunk.replace(' ', '')
        
        if not re.match(r'^-?\d+[hmHM]', cleaned_chunk):
            raise ValueError(f"Invalid time format component: {chunk}")
            
        # Check which unit is present
        has_h = 'h' in cleaned_chunk.lower() or 'hr' in cleaned_chunk.lower()
        has_m = 'm' in cleaned_chunk.lower() and ('min' not in cleaned_chunk.lower())
        
        if has_h and has_m:
            raise ValueError("Mixed units (hours and minutes) must be separated by an operator")
            
        val, unit_type = 0, ''
        
        # Extract number and sign logic specifically for this chunk format like "1h" or "-2 hours"
        num_match = re.match(r'^(-?\d+)', cleaned_chunk)
        if not num_match:
            raise ValueError(f"No valid time value found in {chunk}")
            
        val_str = num_match.group(1)
        sign_char = '+' # Default
        
        # Look for explicit operator inside the chunk string itself? 
        # Usually format is "2h 30m" or "2h+30m". If separated by space, it's one unit.
        
        if has_h:
            val_str += 'h'
            total_seconds += int(val_str) * 3600
            
        elif has_m:
            # Handle minutes carefully as they might be part of a larger string like "1h+2m" 
            # where the split didn't catch it correctly if no space around +
            
            val = int(num_match.group(1))
            sign_char = '+'
            
            # Check for explicit operator before this chunk? No, we already handled that.
            # Just assume positive unless there's a negative number
            
            total_seconds += abs(val) * 60 if unit_type == 'm' else val
        
        elif has_h:
             pass

    return int(total_seconds / 3600)

def aggregate_time_durations(durations: List[str]) -> float:
    """
    Aggregates a list of time difference strings into total seconds.
    
    Args:
        durations (List[str]): List of duration strings like ["1h", "45m", "-2h 30m"]
        
    Returns:
        float: Total duration in seconds
        
    Raises:
        ValueError: If any string cannot be parsed or format is invalid.
    """
    
    total_seconds = 0

if __name__ == '__main__':
    pass
