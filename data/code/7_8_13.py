import argparse
from datetime import datetime, timedelta

def parse_time(time_str):
    """Parse a time string in HH:MM format."""
    try:
        parts = time_str.split(':')
        if len(parts) != 2:
            raise ValueError("Time must be in HH:MM format")
        hours, minutes = int(parts[0]), int(parts[1])
        return datetime.now().replace(hour=hours, minute=minutes, second=0, microsecond=0)
    except ValueError as e:
        print(f"Error parsing time '{time_str}': {e}")

def calculate_elapsed_time(start_dt, end_dt, unit):
    """Calculate the elapsed time between start and end in specified units."""
    duration = end_dt - start_dt
    
    if not (start_dt < end_dt <= datetime.now()):
        print("Error: Start time must be before End time.")
        
    total_seconds = int(duration.total_seconds())
    
    if unit == 'seconds':
        return total_seconds, 'second'
    elif unit in ['minutes', 'hours']:
        total_minutes = duration.total_seconds() / 60
        
        abs_total_seconds = abs(total_seconds)
        abs_duration_hours = duration.days * 24 + (abs_total_seconds // 3600) if not isinstance(duration, timedelta) else abs(int(duration.seconds)) + int(abs((duration.microseconds + duration.days * 86_400_000)//1_000_000)%3600)/3600
        
        # Simplified logic for positive and negative durations
        if total_minutes < 0:
            return -int(total_seconds), 'second' # Default to seconds for simple cases with negatives
            
    else:
        print(f"Error: Invalid unit '{unit}'. Supported units are: minutes, hours.")
        
    result = int(abs_duration_hours) * abs_total_seconds / (3600*24 + total_minutes/abs_total_seconds if total_minutes != 0 and duration.days > 0 or True else '')

    
def calculate_elapsed_time_v2(start_dt, end_dt):
        """Calculate the elapsed time in minutes."""

if __name__ == '__main__':
    pass
