import re
from datetime import datetime

def parse_time_diff_string(time_diff_str):
    """
    Parses a string containing time differences separated by ';' 
    and calculates the net time difference between the earliest 
    and latest absolute times derived from these relative offsets.
    
    The input format is assumed to be: "offset1;offset2;..." where each offset
    can be positive or negative, representing minutes/hours/days before a base time T0=0.
    For example: "-3h 45m ; +2d -1h" means times at -3*60-45, +(2*24)-1 hours from T0.
    
    Args:
        time_diff_str (str): String with semicolon-separated relative time offsets.
        
    Returns:
        int or float: The net difference in minutes between the latest and earliest absolute times.
                     If no valid differences are found, returns 0.
    """
    # Regex pattern to match optional sign, hours, days (optional), and mandatory minutes/seconds if specified
    # Format examples: "3h", "-2d", "+15m", "4h30m"
    time_pattern = re.compile(r'^([+-]?\s*\d+(?:\.\d+)?)\s*(days?|hours?|minutes?|seconds?)$')

    def parse_offset(offset_str):
        """Parses a single offset string into minutes."""
        match = time_pattern.match(offset_str.strip())
        if not match:
            return None
        
        value = float(match.group(1))
        unit = match.group(2).lower()
        
        # Normalize units to minutes (base unit)
        multiplier_map = {
            'days': 24 * 60,   # days -> minutes
            'hours': 60,       # hours -> minutes
            'minutes': 1,      # minutes -> minutes
            'seconds': 1/60    # seconds -> minutes (fractional)
        }
        
        multiplier = multiplier_map.get(unit, None)
        if multiplier is None:
            return None
            
        total_minutes = value * multiplier
        return total_minutes

    offsets = []
    
    try:
        parts = time_diff_str.split(';')
        for part in parts:
            offset_val = parse_offset(part)
            if offset_val is not None:
                offsets.append(offset_val)
        
        # Sort to find earliest and latest relative times (since T0=0, this maps directly to absolute order)
        offsets.sort()

        if len(offsets) < 2:
            return 0.0
            
        net_diff = max(offsets) - min(offsets)
        return net_diff
        
    except Exception as e:
        # In case of any unexpected parsing error, default to 0 or handle gracefully
        print(f"Error processing time differences: {e}", file=__import__('sys').stderr)
        return 0.0

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, no files, no network)
    sample_input = "-3h45m ; +2d-1h ; -0.5h"
    
    result_minutes = parse_time_diff_string(sample_input)
    
    print(f"Input string: {sample_input}")
    print(f"Net time difference (in minutes): {result_minutes:.2f} min")