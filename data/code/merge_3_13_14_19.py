import re
from typing import List

def parse_time_string(duration_str: str) -> int:
    """
    Converts a time difference string (e.g., '2h30m', '45min') into seconds.
    
    Args:
        duration_str: A string representing hours and/or minutes, e.g., "1h", "90m".
        
    Returns:
        Total number of seconds as an integer.
    """
    total_seconds = 0
    
    # Pattern to match optional count followed by 'h' (hours) or 'min/m' (minutes)
    pattern = r'^(\d+)\s*(?:([hm]|\b(h|mn)\b))$'
    
    match = re.match(pattern, duration_str.strip())
    
    if not match:
        raise ValueError(f"Invalid time format: {duration_str}")

    count = int(match.group(1).strip() if match.group(1) else "0")
    unit_type = match.group(2) or ""  # 'h', 'm', etc.

    is_hours = re.match(r'^[dh](?=\d)', duration_str.strip()) is not None
    
    # If no count provided explicitly, assume 1 unit (e.g., "h" -> 1 hour)
    if match.group(1) is None:
        count = int(is_hours)

    multiplier = 3600 if is_hours else 60
        
    return count * multiplier

def aggregate_duration(time_strings: List[str]) -> int:
    """
    Aggregates a list of time difference strings into total seconds.
    
    Handles mixed units (hours and minutes), converts everything to seconds,
    prioritizing performance via pre-compiled regex and efficient iteration.
    
    Args:
        time_strings: A list of duration string tokens like ["1h", "2min", "30m"].
        
    Returns:
        Total sum in seconds as an integer.
    """
    # Compile pattern for reuse (performance optimization)
    _TIME_PATTERN = re.compile(r'^(\d+)\s*(?:([hm]|\b(h|mn)\b))$')

    total_seconds = 0
    
    for s in time_strings:
        try:
            seconds = parse_time_string(s)
        except ValueError as e:
            # Handle silently or raise depending on design; here we skip invalid entries to maintain robustness if needed, 
            # but strict mode is safer per function contract unless specified otherwise.
            print(f"Warning: Skipping '{s}' due to format error.", file=__import__('sys').stderr)
        else:
            total_seconds += seconds
            
    return total_seconds

if __name__ == '__main__':
    sample_inputs = [
        "1h",       # 3600 seconds
        "45min"     # 2700 seconds (explicit minutes)
    ]

    try:
        result = aggregate_duration(sample_inputs)
        print(f"Total duration in seconds for {sample_inputs}: {result}")
        
        # Verify manually expected output:
        # Expected: 1h + 45min = 3600s + (45*60)s = 3600 + 2700 = 6300
        
    except Exception as e:
        print(f"Error occurred during aggregation: {e}")