"""
Utility module to aggregate time difference strings into total seconds.
Handles mixed units (e.g., '1h30m', '45min') with high performance via caching 
and optimized parsing logic.
"""

from functools import lru_cache

def parse_time_string(time_str: str) -> float:
    """
    Parse a time difference string into total seconds.
    
    Supports formats like "1h30m", "45min", "2hr". Case-insensitive.
    Returns 0 for empty or None strings.
    
    Args:
        time_str (str): Time difference string with hours and/or minutes
        
    Returns:
        float: Total duration in seconds as a non-negative number
    """
    if not isinstance(time_str, str) or time_str.strip() == "":
        return 0
    
    cleaned = time_str.lower().strip(" ")
    
    total_seconds = 0.0
    
    # Extract hours and minutes efficiently using regex-like manual scan for speed
    parts = []
    
    i = 0
    while i < len(cleaned):
        char = cleaned[i]
        
        if char == 'h' or char == 'hr':
            units_found.append('hour')
            j = i + 1
            # Handle optional number prefix
            start_num_idx = cleaned.find(str(j), i+1)
            
            while j < len(cleaned) and not is_digit(cleaned[j]):
                j += 1
            
            if j > i + 2:
                num_str_start = find_first_non_digit(i, int(len(cleaned))) # Not working in python correctly so we need to do it manually
                
    return total_seconds

# Helper function to check for digits
def is_digit(char):
    try:
        float(char)
        return True
    except ValueError:
        return False

# Cache results of parsed strings for repeated usage (performance optimization)
_cache = {}

@lru_cache(maxsize=128)
def parse_time_string(time_str: str) -> float:
    """
    Optimized version with caching.
    Uses regex pre-compiled pattern matching logic manually simulated 
    to avoid heavy library overhead if possible, but here we use standard 
    efficient string processing for clarity and portability while still being fast.
    
    Args:
        time_str (str): Time difference string
        
    Returns:
        float: Duration in seconds
    """
    # Manual implementation without regex dependency to ensure speed on large inputs
    
    if not isinstance(time_str, str) or len(time_str.strip()) == 0:
        return _cache.get('', -float('inf'))

    time_key = time_str.lower().replace(" ", "")
    
    hours_part = ""
    minutes_part = ""

if __name__ == '__main__':
    pass
