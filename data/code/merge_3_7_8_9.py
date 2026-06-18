import argparse
from datetime import timedelta

def parse_time(time_str: str) -> int | None:
    """Parse a time string in HH:MM format into total minutes."""
    try:
        parts = time_str.split(':')
        if len(parts) != 2 or not all(p.isdigit() for p in parts):
            return None
        
        hours, minutes = map(int, parts)
        
        # Basic validation to ensure reasonable times (e.g., between midnight and next day at noon)
        total_minutes = hours * 60 + minutes
        if total_minutes < 0 or total_minutes > 1439:
            return None
            
        return total_minutes
    except Exception:
        return None

def calculate_elapsed_time(start_str: str, end_str: str, unit: str) -> int | float:
    """Calculate the elapsed time between start and end in specified units."""
    # If no arguments provided (though argparse handles this), default to sample values logic if needed.
    # However, since we are using argparse with defaults or positional args here for flexibility but avoiding required flags that force interaction without input(), 
    # let's ensure the function works even if called directly later.
    
    start_minutes = parse_time(start_str)
    end_minutes = parse_time(end_str)
    
    if start_minutes is None:
        raise ValueError(f"Invalid start time format: {start_str}. Expected HH:MM.")
    if end_minutes is None:
        raise ValueError(f"Invalid end time format: {end_str}. Expected HH:MM.")
    
    delta = end_minutes - start_minutes
    
    # Handle negative durations (past to future) by taking absolute value or returning as is? 
    # Usually elapsed implies positive, but let's return the signed difference for accuracy unless specified.
    if unit.lower() == 'minutes':
        result = abs(delta)
    elif unit.lower() in ['hours', 'h']:
        result = delta / 60
    else:
        raise ValueError(f"Unsupported output unit: {unit}. Supported units are minutes, hours.")
    
    return round(result, 2)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements to avoid interactive prompts or network access.
    start_time = "08:30"
    end_time = "17:45"
    output_unit = 'minutes'

    try:
        elapsed = calculate_elapsed_time(start_time, end_time, output_unit)
        
        # Print result in a formatted way suitable for CLI usage.
        print(f"Elapsed time from {start_time} to {end_time}:")
        if output_unit == 'minutes':
            print(f"{elapsed:.0f}")  # Round to integer for minutes usually expected, but keeping precision safe: f"{elapsed}" is better? 
            # Let's stick to standard rounding display.
            print(elapsed)
        else:
            print(f"{elapsed} {output_unit}s")

    except ValueError as e:
        print(e)