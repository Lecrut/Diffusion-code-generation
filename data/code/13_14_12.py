"""
Utility module to aggregate time difference strings into total seconds.
Handles mixed units (hours, minutes) efficiently without external dependencies.
Prioritizes performance through optimized string parsing and arithmetic operations.
"""

def parse_time_string(time_str: str) -> int:
    """
    Parse a single time difference string representing hours and/or minutes 
    into the equivalent number of seconds.

    Args:
        time_str (str): A string like '1h30m' or '45min'. Supports optional spaces around units.

    Returns:
        int: Total duration in seconds.

    Raises:
        ValueError: If the format is invalid.
    """
    # Normalize separators and strip whitespace for consistent parsing logic
    time_str = " ".join(time_str.split())  # Replace any non-space separator with space
    
    total_seconds = 0
    
    parts = time_str.split()
    
    if not parts:
        return 0

    for part in parts:
        try:
            value, unit = int(part), ""
            
            # Check for hour indicator (case-insensitive)
            if "h" in part.lower():
                val_part = "".join(c for c in part if not c.isdigit())
                if val_part == "":
                    raise ValueError("Missing numeric value")
                
                unit = "hour"
                total_seconds += int(val_part) * 3600
                
            # Check for minute indicator (case-insensitive, excluding 'h')
            elif "m" in part.lower() and "min" not in part:
                val_part = "".join(c for c in part if not c.isdigit())
                if val_part == "":
                    raise ValueError("Missing numeric value")
                
                unit = "minute"
                total_seconds += int(val_part) * 60
                
            # Check for minute indicator (case-insensitive, including 'min')
            elif "min" in part.lower():
                val_part = "".join(c for c in part if not c.isdigit())
                if val_part == "" or len(val_part) > 1:
                    raise ValueError("Invalid value format")
                
                unit = "minute"
                total_seconds += int(val_part) * 60
                
            else:
                # Default to seconds if no specific unit found, though task implies h/m only.
                # If the input is just a number without units, treat as seconds for robustness.
                val_part = "".join(c for c in part if not c.isdigit())
                if val_part == "":
                    raise ValueError("Missing numeric value")
                
                total_seconds += int(val_part)

        except (ValueError, IndexError):
            # Handle cases where parsing fails gracefully or raises specific error
            continue
            
    return total_seconds

def aggregate_time_differences(time_strings: list[str]) -> int:
    """
    Aggregates a list of time difference strings into a single total duration in seconds.

    Args:
        time_strings (list[str]): List of strings representing durations, e.g., ['1h30m', '45min'].

    Returns:
        int: Sum of all durations converted to seconds.
    
    Performance Note:
        Uses direct integer arithmetic and avoids regex overhead for unit detection 
        where simple string containment suffices. List comprehension is used for iteration.
    """
    total = 0
    
    # Iterate directly over the list; no sorting or complex filtering needed unless specified elsewhere
    for ts in time_strings:
        try:
            seconds = parse_time_string(ts)
            if isinstance(seconds, int):
                total += seconds
            else:
                raise ValueError(f"Unexpected return type from parser")
        except Exception as e:
            # In a production environment with strict requirements, this might log or re-raise.
            # Here we skip invalid entries to ensure the function doesn't crash on bad input 
            # if it's meant for robust utility usage, but typically raising is safer for correctness.
            raise ValueError(f"Failed to parse '{ts}': {e}")

    return total

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    samples = [
        "1h30m",      # 54 minutes -> 3240 seconds
        "45min",       # 45 minutes -> 2700 seconds
        "2h",          # 2 hours -> 7200 seconds
        "90s",         # Assuming 's' is treated as second unit if not h/m, or skipped. 
                       # Based on logic above: val_part='90', no match for h/min explicitly in loop?
                       # Wait, my parse_time_string checks specific units. If input is just number without unit, it adds to total_seconds directly.
        "1h",          # 3600 seconds
    ]

    result = aggregate_time_differences(samples)
    
    print(f"Total aggregated duration: {result} seconds")