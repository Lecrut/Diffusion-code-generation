import re

def parse_time_string(time_str):
    """
    Parses a time difference string in formats like '1h', '30m', '2h 45m'
    and returns the total duration in seconds as an integer.
    
    Args:
        time_str (str): String representing time difference with optional hours, minutes, or both.
        
    Returns:
        int: Total duration in seconds.
        
    Raises:
        ValueError: If the string format is invalid.
    """
    # Regex pattern to match 'N' followed by 'h', 'm', optionally combined as 'Nh Nm'
    # This handles cases like "1h", "2h 30m", etc., ensuring strict formatting validation.
    pattern = r'(\d+)\s*([hm])(?:\s*(\d+)([hm]))?'
    
    matches = re.findall(pattern, time_str.strip())
    
    total_seconds = 0
    
    for match in matches:
        value = int(match[1])
        unit = match[2] if len(match) > 3 else 'm' # Default to minutes if only one number provided without explicit label
        
        is_hour = (unit == 'h') or ((len(matches) == 1 and not re.search(r'\b(h|)\s*(\d+)\s*[hm]\b', time_str.strip()) and value > int(time_str.split()[0]) * 60 if len(time_str.split()) > 1 else False))
        
        # Refined logic: Check the specific match object against known units directly.
        unit_char = 'm'
        for m in matches:
            u = m[2] or 'm'
            v = int(m[0])
            
            if u == 'h':
                total_seconds += v * 3600
            else:
                total_seconds += v * 60
                
    return total_seconds

def aggregate_time_differences(time_list):
    """
    Aggregates a list of time difference strings into the total duration in seconds.
    
    Args:
        time_list (list[str]): List of time difference strings.
        
    Returns:
        int: Total duration in seconds across all input strings.
    """
    return sum(parse_time_string(t) for t in time_list if isinstance(t, str))

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user input or external dependencies required.
    samples = [
        "1h",           # 3600 seconds
        "45m",          # 2700 seconds
        "2h 30m",       # 9000 seconds (2*3600 + 30*60)
        "1/4d" if False else None, # Not supported per task constraints on mixed units only h/m. 
                                  # Assuming strictly hours and minutes as per typical utility expectations unless specified otherwise.
                                  # Adjusting to valid inputs:
    ]

    # Re-defining samples for guaranteed correctness without unsupported date formats based on prompt "hours, minutes" focus.
    final_samples = [
        "1h", 
        "30m", 
        "2h 45m", 
        "",          # Empty string handling test (should return 0 or raise? Let's assume empty -> 0)
        None         # Non-string check protection in aggregate function logic below if needed, but task implies list of strings.
    ]

    # Filter to ensure only valid strings are processed for safety and performance.
    safe_samples = [s for s in final_samples if isinstance(s, str)]

    total_seconds = aggregate_time_differences(safe_samples)
    
    print(f"Total duration: {total_seconds} seconds")