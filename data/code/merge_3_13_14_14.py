import re

def parse_duration_string(s: str) -> int:
    """
    Converts a time difference string like 'h:mm', 'm:ss' or 'd:h:m's into total seconds.
    Prioritizes performance by using regex and direct arithmetic without heavy libraries.
    
    Args:
        s (str): Time difference string with mixed units (hours, minutes).
        
    Returns:
        int: Total duration in seconds.
    """
    # Regex to capture hours, minutes, seconds if present
    pattern = r'(\d+(?:\.\d+)?)?\s*(h|hr)?(?:m|min)?(s|sec)?'
    
    matches = re.findall(pattern, s.replace(',', ''))
    
    total_seconds = 0
    
    for val_type in matches:
        if not all(val_type):
            continue
            
        value_str, unit_suffix = val_type[1], val_type[-1]
        
        try:
            numeric_val = float(value_str)
        except ValueError:
            # Handle cases where there is a number but no suffix or vice versa gracefully by defaulting to 0 if ambiguous in simple string format
            continue
            
        duration_in_seconds = 0
        
        # Check for hours (h, hr) and minutes (m, min), seconds (s, sec) handling.
        
        val_unit_suffix_lower = unit_suffix.lower()
        
        has_hour_flag = bool(re.search(r'h|hr', s)) or len([x for x in val_type if 'hour' in str(x)]) > 0 # heuristic based on string content check as per requirement
        
        def compute_seconds(val, unit):
            nonlocal total_seconds

if __name__ == '__main__':
    pass
